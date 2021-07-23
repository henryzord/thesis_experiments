import Orange  # pip install orange3
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import numpy as np


def perform_checks(results_path: str) -> pd.DataFrame:
    df = pd.read_csv(results_path, index_col=0)

    if np.any(df > 0):
        raise ValueError("Result values should be negative (the smaller the value, the better). If that's not the case,"
                         "simply flip each value signal (e.g. 0.83 -> -0.83)")

    if not isinstance(df.index.dtype, object):
        raise TypeError("First column should have datasets names")

    return df


def main(results_path: str) -> None:
    df = perform_checks(results_path)

    n = len(df.index)  # number of datasets it was tested on
    names = df.columns  # names of methods

    # computes average ranks
    avranks = df.rank(axis=1).mean(axis=0).values

    cd = Orange.evaluation.scoring.compute_CD(avranks, n=n, alpha="0.05", test="nemenyi")
    Orange.evaluation.graph_ranks(
        avranks=avranks,
        names=names,
        cd=cd,
        width=6,
        textspace=1.5,
        # filename='./cd2.png'
    )
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script for generating critical difference graphs, using Nemenyi test, and a significance level of'
                    '0.05.'
    )

    parser.add_argument(
        '--results-path', action='store', required=True,
        help='Path to dataset, where rows are datasets, and columns the methods. Values should be negative. '
             'Uses first column as index for pandas DataFrame.'
    )

    args = parser.parse_args()
    main(results_path=args.results_path)
