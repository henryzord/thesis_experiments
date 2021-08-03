# README

Use `generate_partitions.py` on the [datasets of AUTOCVE EVOSTAR paper](https://github.com/celiolarcher/autocve_experiments/tree/main/experiments_EVOSTAR21/datasets).

the `dict_conversion.json` file converts IDs of datasets to human-readable names.

`get_most_used_hyperparameters.py` do what it says: gets the most "popular" hyper-parameters of both PBIL and EDNEL from the nested cross-validation experiment. 

Use `postprocess_holdout.py` to compile experiment results, once finished.