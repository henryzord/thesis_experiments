# from sklearn.metrics import accuracy_score, balanced_accuracy_score
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd

import sys
import os
import time
import subprocess
import shutil

TIME_PER_TASK=5400
GRACE_PERIOD=100

import argparse


def parse_open_ml(datasets_path, d_id, seed):
    df = pd.read_csv(os.path.join(datasets_path, '{0}.csv').format(d_id))
    df_types = pd.read_csv(os.path.join(datasets_path, '{0}_types.csv').format(d_id))

    df_valid = df[~df['target'].isnull()]

    x_cols = [c for c in df_valid.columns if c != 'target']
    X = df_valid[x_cols]
    y = df_valid['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)

    return X_train, X_test, y_train, y_test, df_types


def main(args):
    SEED_LIST = [5249444, 7592240, 4510071, 2688207, 5344429, 6581462, 6381116, 4901935, 1977886, 2591851, 9404208, 4098546]  # 12 values, will use only 10
    list_exp=[15, 37, 307, 451, 458, 469, 1476, 1485, 1515, 1590, 6332, 23517, 40496, 40499, 40994]  # 15 values/datasets

    N_TRIALS = 10  # 10 runs of holdout, per evostar paper

    for id_exp in list_exp:

        dataset_types = pd.read_csv(os.path.join(args.datasets_path, '%d_types.csv' % id_exp))
        a = np.flatnonzero(np.logical_or(dataset_types['TYPE'] == 'categorical', dataset_types['TYPE'] != 'numerical'))
        str_process = ','.join(map(lambda x: str(x + 1), a))
        
        for id_trial in range(N_TRIALS):
            X_train, X_test, y_train, y_test, df_types = parse_open_ml(args.datasets_path, id_exp, SEED_LIST[id_trial])

            train = X_train.join(y_train)
            test = X_test.join(y_test)
            
            train.to_csv(os.path.join(args.write_path, 'dataset_%d_trial_%02d_train.csv' % (id_exp, id_trial + 1)), index=False)
            test.to_csv(os.path.join(args.write_path, 'dataset_%d_trial_%02d_test.csv' % (id_exp, id_trial + 1)), index=False)

            with open(os.path.join(args.write_path, 'dataset_%d_trial_%02d_train_temp.arff' % (id_exp, id_trial + 1)), 'w') as write_file:
                subprocess.run([
                    "java", "-classpath", "C:\\Users\\henry\\weka-3-9-3\\weka.jar", "weka.core.converters.CSVLoader", 
                    os.path.join(args.write_path, 'dataset_%d_trial_%02d_train.csv' % (id_exp, id_trial + 1)), ">", 
                    os.path.join(args.write_path, 'dataset_%d_trial_%02d_train_temp.arff' % (id_exp, id_trial + 1))
                ], stdout=write_file)

            with open(os.path.join(args.write_path, 'dataset_%d_trial_%02d_test_temp.arff' % (id_exp, id_trial + 1)), 'w') as write_file:
                subprocess.run([
                    "java", "-classpath", "C:\\Users\\henry\\weka-3-9-3\\weka.jar", "weka.core.converters.CSVLoader", 
                    os.path.join(args.write_path, 'dataset_%d_trial_%02d_test.csv' % (id_exp, id_trial + 1)), ">", 
                    os.path.join(args.write_path, 'dataset_%d_trial_%02d_test_temp.arff' % (id_exp, id_trial + 1))
                ], stdout=write_file)

            subprocess.run([
                "java", "-classpath", "C:\\Users\\henry\\weka-3-9-3\\weka.jar", "weka.filters.unsupervised.attribute.NumericToNominal", "-R", str_process, 
                "-i", os.path.join(args.write_path, 'dataset_%d_trial_%02d_train_temp.arff' % (id_exp, id_trial + 1)), 
                "-o", os.path.join(args.write_path, 'dataset_%d_trial_%02d_train.arff' % (id_exp, id_trial + 1)) 
            ])

            subprocess.run([
                "java", "-classpath", "C:\\Users\\henry\\weka-3-9-3\\weka.jar", "weka.filters.unsupervised.attribute.NumericToNominal", "-R", str_process, 
                "-i", os.path.join(args.write_path, 'dataset_%d_trial_%02d_test_temp.arff' % (id_exp, id_trial + 1)), 
                "-o", os.path.join(args.write_path, 'dataset_%d_trial_%02d_test.arff' % (id_exp, id_trial + 1)) 
            ])

            os.remove(os.path.join(args.write_path, 'dataset_%d_trial_%02d_train.csv' % (id_exp, id_trial + 1)))
            os.remove(os.path.join(args.write_path, 'dataset_%d_trial_%02d_test.csv' % (id_exp, id_trial + 1)))

            os.remove(os.path.join(args.write_path, 'dataset_%d_trial_%02d_train_temp.arff' % (id_exp, id_trial + 1)))
            os.remove(os.path.join(args.write_path, 'dataset_%d_trial_%02d_test_temp.arff' % (id_exp, id_trial + 1)))

            print('Done: dataset %d trial %02d' % (id_exp, id_trial + 1))

#            break  # TODO remove
#        break  # TODO remove
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Converts datasets used by AUTOCVE to a format usable to PBIL and EDNEL.'
    )

    parser.add_argument(
        '--datasets-path', action='store', required=True,
        help='Path to where all .csv datasets are stored'
    )

    parser.add_argument(
        '--write-path', action='store', required=True,
        help='Path to where write converted datasets.'
    )

    _some_args = parser.parse_args()

    main(args=_some_args)
