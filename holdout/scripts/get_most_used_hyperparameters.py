import numpy as np
import pandas as pd

import os

import argparse
from collections import Counter


def group_hyperparameters(columns):
    splitted = list(map(lambda x: x.split('_'), columns))

    sets = dict()

    # groups columns by hyper-parameter name
    for i in range(len(splitted)):
        sets[i] = list()

        sets[i].append('_'.join(splitted[i]))
        for j in range(len(splitted)):
            if (i != j) and (
                    len((set(splitted[i]) - set(splitted[j])).union(set(splitted[j]) - set(splitted[i]))) == 2):
                sets[i].append('_'.join(splitted[j]))

    grouped = [y.split('|') for y in set(list(map(lambda x: '|'.join(sorted(x)), sets.values())))]
    return grouped


def main(args):
    df = pd.read_csv(args.file_path, index_col=0)

    grouped = group_hyperparameters(df.columns)

    for hyper in grouped:
        param_name = '_'.join(hyper[0].split('_')[:-1])

        sub = df[hyper].sum()
        print('%s: %s with %.2f uses' % (param_name, sub.index[sub.argmax()].split('_')[-1], sub[sub.argmax()]/sub.sum()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gets most used hyper-parameters on nested cross-validation procedure.'
    )

    parser.add_argument(
        '--file-path', action='store', required=True,
        help='Path to .csv with hyper-parameters.'
    )

    _some_args = parser.parse_args()

    main(args=_some_args)
