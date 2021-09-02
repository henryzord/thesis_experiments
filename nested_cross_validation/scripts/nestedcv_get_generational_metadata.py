import argparse
import os
import subprocess
import pandas as pd
import numpy as np


def main(experiment_path: str):
    algorithms = [x for x in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, x)) and 'script' not in x]

    dfs = dict()
    for algorithm in algorithms:
        try:
            dfs[algorithm] = get_data_for_algorithm(os.path.join(experiment_path, algorithm))
        except Exception:
            pass


def get_data_for_algorithm(experiment_path: str):
    experiments = [x for x in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, x))]

    dict_data = dict()

    for experiment in experiments:
        dataset_name = [x for x in os.listdir(os.path.join(experiment_path, experiment)) if os.path.isdir(os.path.join(experiment_path, experiment, x))][0]

        folders = [x for x in os.listdir(os.path.join(experiment_path, experiment, dataset_name)) if
                   os.path.isdir(os.path.join(experiment_path, experiment, dataset_name, x)) and x != 'overall'
                   ]

        times = []

        for folder in folders:
            df = pd.read_csv(os.path.join(experiment_path, experiment, dataset_name, folder, 'loggerData.csv'))
            times += [df['lap time (seconds)'].sum()]

        dict_data[dataset_name] = np.mean(times)

    all_df = pd.DataFrame.from_dict(data=dict_data, orient='index', columns=['average time on external folds'])
    return all_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='After running experiments (one or more), use this script to generate a summary of the 10-fold '
                    'cross validation procedures. If more than one sample was taken, it will display the mean metrics '
                    'in the document. It also generates a csv with the comparison of all experiments.'
    )

    parser.add_argument(
        '--experiment-path', action='store', required=True,
        help='Either a path to where several experiments are, or the path of a single experiment. Will act according.'
    )

    args = parser.parse_args()
    main(experiment_path=args.experiment_path)


