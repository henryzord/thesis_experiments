"""
Script for measuring how much time has been elapsed (on average) for methods that do not record metadata.
"""

import argparse
import os
import subprocess
import pandas as pd
import numpy as np
from datetime import datetime as dt
from matplotlib import pyplot as plt


def main(experiment_path: str):
    experiments = [x for x in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, x))]

    dict_datasets = {}

    for experiment in experiments:
        dataset_name = [x for x in os.listdir(os.path.join(experiment_path, experiment)) if os.path.isdir(os.path.join(experiment_path, experiment, x))][0]

        preds_files = [x for x in os.listdir(os.path.join(experiment_path, experiment, dataset_name, 'overall')) if '.preds' in x]

        list_times = []

        for some_file in preds_files:
            time = os.path.getmtime(os.path.join(experiment_path, experiment, dataset_name, 'overall', some_file))
            file_creation_time = dt.fromtimestamp(time).strftime('%Y-%m-%d-%H-%M-%S')

            dt_begin = dt.strptime(experiment, '%Y-%m-%d-%H-%M-%S')
            dt_file = dt.strptime(file_creation_time, '%Y-%m-%d-%H-%M-%S')

            # 12 combinations of hyper-parameters * 5 internal folds
            difference = (dt_file - dt_begin).total_seconds() / (12 * 5)  # TODO code to be used for nested-cross validation
            # difference = (dt_file - dt_begin).total_seconds()   # TODO code to be used for holdout
            list_times += [difference]

        dict_datasets[dataset_name] = list_times

        local_df = pd.DataFrame(list_times, columns=['times'])
        print('summary for dataset %s:' % dataset_name)
        print(local_df.describe())

    all_df = pd.DataFrame(dict_datasets)
    all_df = all_df[sorted(all_df.columns, reverse=True)]
    all_df.boxplot(grid=False, vert=False)
    plt.xlabel('Time to run (in seconds)')
    plt.xticks([x * 360 for x in range(11)])  # TODO remove if using holdout
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script for measuring how much time has been elapsed (on average) for methods that do not record '
                    'metadata.'
    )

    parser.add_argument(
        '--experiment-path', action='store', required=True,
        help='Either a path to where several experiments are, or the path of a single experiment. Will act according.'
    )

    args = parser.parse_args()
    main(experiment_path=args.experiment_path)


