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
from matplotlib.cm import viridis
from matplotlib.colors import to_hex
import matplotlib.patches as mpatches


def main(algorithms_path: str):
    algorithms = algorithms_path.split(';')

    algorithm_data = dict()
    datasets_sets = set()

    for experiment_path in algorithms:
        algorithm_name = experiment_path[(experiment_path.index(']') + 1):experiment_path.rindex('[')].strip()
        algorithm_data[algorithm_name] = dict()

        experiments = [x for x in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, x))]

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
                difference = (dt_file - dt_begin).total_seconds() / (12 * 5)
                list_times += [difference]

            algorithm_data[algorithm_name][dataset_name] = list_times
            datasets_sets = datasets_sets.union({dataset_name})

    all_df = pd.DataFrame(
        index=pd.MultiIndex.from_product([sorted(list(datasets_sets)), np.arange(10)], names=['dataset', 'id']),
        columns=sorted(list(algorithm_data.keys())),
        dtype=float
    )

    for some_algorithm in algorithm_data.keys():
        for some_dataset in algorithm_data[some_algorithm].keys():
            all_df.loc[(some_dataset, slice(None)), some_algorithm] = algorithm_data[some_algorithm][some_dataset]

    border = 30
    max_time = all_df.max().max() + border
    colors = list(map(to_hex, viridis(np.linspace(0, 1, len(all_df.columns)))))

    # from quickest dataset to slowest
    dataset_order = all_df.groupby(axis='index', level=0).mean().mean(axis=1).sort_values().index.tolist()[::-1]

    fig, ax = plt.subplots()

    for i, algorithm in enumerate(all_df.columns):
        averages = all_df[algorithm].groupby(level=0).mean().loc[dataset_order]
        ax.scatter(
            averages,
            np.arange(i, len(averages) * len(all_df.columns), len(all_df.columns)),
            label=algorithm,
            color=colors[i])

    for j in range(0, len(dataset_order) * len(all_df.columns), len(all_df.columns)):
        if j % 2 == 0:
            rect = mpatches.Rectangle(
                xy=(0 - border, j - 0.5),
                width=max_time + border,
                height=len(all_df.columns),
                fill=True,
                color="#CCCCCC",
                alpha=0.5,
                zorder=0
            )
            plt.gca().add_patch(rect)


    ax.set_yticks(np.arange(1, len(dataset_order) * len(all_df.columns), len(all_df.columns)))
    ax.set_yticklabels(dataset_order)
    #
    ax.set_xlim(0 - border, max_time)
    ax.set_ylim(-0.5, len(dataset_order) * len(all_df.columns) + 0.5)

    ax.set_xlabel('Time to run (in seconds)')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script for measuring how much time has been elapsed for algorithms. Will use file metadata to measure it'
    )

    parser.add_argument(
        '--experiment-path', action='store', required=True,
        help='Multiple paths, separated by semicolons, of algorithms from which will extract elapsed time values from metadata'
    )

    args = parser.parse_args()
    main(algorithms_path=args.experiment_path)
