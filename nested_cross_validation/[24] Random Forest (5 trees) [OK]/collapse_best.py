import os
import json
import time
import argparse
import numpy as np
from datetime import datetime as dt
from scipy.io import arff
import math as Math

dict_conversion = {
    'bagSizePercent': '-P %s',
    'numIterations': '-I %s',
    'breakTiesRandomly': {
        'value': '-B',
        'presenceMeans': True
    },
    'maxDepth': '-depth %s',
    'numFeatures': '-K %s',
}


def main(args):
    classifiers = [x for x in os.listdir('.') if os.path.isdir(os.path.join('.', x))]

    ev = dict()

    max_fold = -1
    min_fold = np.inf

    for clf in classifiers:
        experiment_folders = [x for x in os.listdir(os.path.join('.', clf)) if os.path.isdir(os.path.join('.', clf, x))]

        for experiment_folder in experiment_folders:
            dataset_name = [x for x in os.listdir(os.path.join('.', clf, experiment_folder)) if
                            os.path.isdir(os.path.join('.', clf, experiment_folder, x))][0]

            if dataset_name not in ev:
                ev[dataset_name] = dict()
            if clf not in ev[dataset_name]:
                ev[dataset_name][clf] = dict()

            parameter_files = [x for x in os.listdir(os.path.join('.', clf, experiment_folder, dataset_name)) if
                               os.path.isfile(os.path.join('.', clf, experiment_folder, dataset_name, x))]

            for parameter_file in parameter_files:
                n_fold = int(
                    parameter_file[parameter_file.index('fold-') + len('fold-'):parameter_file.index('_parameters')])
                max_fold = max(n_fold, max_fold)
                min_fold = min(n_fold, min_fold)

                with open(os.path.join('.', clf, experiment_folder, dataset_name, parameter_file), 'r') as some_file:
                    metadata = json.load(some_file)
                    del metadata["dataset_name"]
                    del metadata["dataset_experiment_path"]
                    ev[dataset_name][clf][n_fold] = metadata

    # now builds the dictionary of hyper-parameters
    final = dict(((x, dict()) for x in ev.keys()))
    for dataset_name in final.keys():
        final[dataset_name] = dict(((x, '') for x in range(min_fold, max_fold + 1)))

        n_attributes = None

        for n_fold in range(min_fold, max_fold + 1):

            if n_attributes is None:
                with open(os.path.join(args.datasets_path, dataset_name, '%s-10-%dtra.arff' % (dataset_name, n_fold)), 'r') as arff_file:
                    array, metadata = arff.loadarff(arff_file)
                    n_attributes = len(array.dtype) - 1

            for clf in ev[dataset_name].keys():
                final[dataset_name][n_fold] += '-RandomForestRulesClassifier '

                for param_name, param_value in ev[dataset_name][clf][n_fold].items():  # type: str
                    converted = dict_conversion[param_name]
                    if isinstance(converted, dict):
                        param_value_b = True if param_value in ['true', 'True'] else False

                        if param_value_b:
                            if converted['presenceMeans']:
                                final[dataset_name][n_fold] += converted['value'] + ' '
                            else:
                                pass
                        else:
                            if converted['presenceMeans']:
                                pass
                            else:
                                final[dataset_name][n_fold] += converted['value'] + ' '
                    else:
                        if param_name == 'numFeatures':
                            final[dataset_name][n_fold] += (dict_conversion[param_name] % round(eval(param_value[param_value.index('{')+1:param_value.index('}')].replace('p', str(n_attributes))))) + ' '
                        else:
                            final[dataset_name][n_fold] += (dict_conversion[param_name] % param_value) + ' '

    print(json.dumps(final, indent=2))
    return final


def run_all(final: dict, args):
    metadata_path = args.metadata_path

    with open(os.path.join(metadata_path, 'script.bat'), 'w') as some_file:

        for dataset_name in final.keys():
            time.sleep(1)
            experiment_folder = dt.now().strftime('%Y-%m-%d-%H-%M-%S')

            os.mkdir(os.path.join(metadata_path, experiment_folder))
            os.mkdir(os.path.join(metadata_path, experiment_folder, dataset_name))
            os.mkdir(os.path.join(metadata_path, experiment_folder, dataset_name, 'overall'))

            this_metadata_path = os.path.join(metadata_path, experiment_folder, dataset_name, 'overall')

            for n_fold in final[dataset_name].keys():
                some_file.write('java -Xmx6G -classpath ednel.jar ednel.utils.analysis.optimizers.RandomSearchApply '
                                '--datasets_path %s --datasets_names %s --metadata_path %s --n_samples 1 --n_fold %d '
                                '--string_options \"%s\"\n' % (args.datasets_path, dataset_name, this_metadata_path,
                                                               n_fold, final[dataset_name][n_fold]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gets best version of each base classifier, for each external fold of each dataset, and ensembles it.'
    )

    parser.add_argument(
        '--metadata-path', action='store', required=True,
        help='Path to where all datasets are stored'
    )

    parser.add_argument(
        '--datasets-path', action='store', required=True,
        help='Path to where all datasets are stored'
    )

    _some_args = parser.parse_args()

    _interpreted = main(_some_args)
    run_all(_interpreted, args=_some_args)
