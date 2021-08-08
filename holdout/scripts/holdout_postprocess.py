import argparse
import os
import subprocess
import pandas as pd
import numpy as np

from pandas.errors import EmptyDataError

from sklearn.metrics import balanced_accuracy_score


def main(experiment_path: str, n_trials: int):
    experiments = [x for x in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, x))]

    scores_per_dataset = dict()

    for experiment in experiments:
        dataset_names = [x for x in os.listdir(os.path.join(experiment_path, experiment)) if os.path.isdir(os.path.join(experiment_path, experiment, x))]
        for dataset in dataset_names:
            scores_per_dataset[dataset] = list()

            overall_folder = os.path.join(experiment_path, experiment, dataset, 'overall')
            file_preds = [x for x in os.listdir(overall_folder) if '.preds' in x]
            if (len(file_preds) % n_trials) != 0:
                if os.path.exists(os.path.join(overall_folder, 'summary_1.csv')):
                    os.remove(os.path.join(overall_folder, 'summary_1.csv'))
                del scores_per_dataset[dataset]
                continue

            for some_file in file_preds:
                try:
                    local_df = pd.read_csv(os.path.join(experiment_path, experiment, dataset, 'overall', some_file), sep=';')
                    y_column = local_df.columns[0]
                    clf_column = local_df.columns[-1]

                    y_true = local_df[y_column].values
                    pred_scores = np.array(local_df[clf_column].apply(lambda x: list(map(float, x.split(',')))).values.tolist())
                    y_pred = pred_scores.argmax(axis=1)

                    balanced_acc = balanced_accuracy_score(y_true, y_pred)
                    scores_per_dataset[dataset] += [balanced_acc]
                except EmptyDataError:  # file is there but is empty
                    if os.path.exists(os.path.join(overall_folder, 'summary_1.csv')):
                        os.remove(os.path.join(overall_folder, 'summary_1.csv'))
                    del scores_per_dataset[dataset]
                    break

    frozen_datasets = list(scores_per_dataset.keys())

    all_df = pd.DataFrame(
        dtype=float,
        index=frozen_datasets,
        columns=['mean', 'std']
    )

    for dataset in frozen_datasets:
        all_df.loc[dataset, 'mean'] = np.mean(scores_per_dataset[dataset])
        all_df.loc[dataset, 'std'] = np.std(scores_per_dataset[dataset])

    all_df.to_csv(os.path.join(experiment_path, 'holdout_summarized.csv'))
    print(all_df)


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

    parser.add_argument(
        '--n-trials', action='store', required=False, type=int, default=10,
        help='Optional: number of ran trials. Defaults to 10'
    )

    args = parser.parse_args()
    main(experiment_path=args.experiment_path, n_trials=args.n_trials)


