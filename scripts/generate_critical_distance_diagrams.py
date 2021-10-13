import Orange  # pip install orange3
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import numpy as np
# import scipy as sp
import scipy.stats as st
import itertools as it


def compute_CD_for_aligned_ranks(avranks, n, alpha="0.05", test="nemenyi"):
    """
    Code adapted from Orange toolkit. Computes CD specific for Friedman aligned ranks.

    --- Original documentation ---

    Returns critical difference for Nemenyi or Bonferroni-Dunn test
    according to given alpha (either alpha="0.05" or alpha="0.1") for average
    ranks and number of tested datasets N. Test can be either "nemenyi" for
    for Nemenyi two tailed test or "bonferroni-dunn" for Bonferroni-Dunn test.
    """
    k = len(avranks)
    d = {("nemenyi", "0.05"): [0, 0, 1.959964, 2.343701, 2.569032, 2.727774,
                               2.849705, 2.94832, 3.030879, 3.101730, 3.163684,
                               3.218654, 3.268004, 3.312739, 3.353618, 3.39123,
                               3.426041, 3.458425, 3.488685, 3.517073,
                               3.543799],
         ("nemenyi", "0.1"): [0, 0, 1.644854, 2.052293, 2.291341, 2.459516,
                              2.588521, 2.692732, 2.779884, 2.854606, 2.919889,
                              2.977768, 3.029694, 3.076733, 3.119693, 3.159199,
                              3.195743, 3.229723, 3.261461, 3.291224, 3.319233],
         ("bonferroni-dunn", "0.05"): [0, 0, 1.960, 2.241, 2.394, 2.498, 2.576,
                                       2.638, 2.690, 2.724, 2.773],
         ("bonferroni-dunn", "0.1"): [0, 0, 1.645, 1.960, 2.128, 2.241, 2.326,
                                      2.394, 2.450, 2.498, 2.539]}
    q = d[(test, alpha)]
    # ( k* (k + 1) / (n * 6.0)) ** 0.5
    # cd = q[k] * (k * (k + 1) / (n * 6.0)) ** 0.5
    cd = q[k] * (k * (n * k + 1) / 6.) ** 0.5
    return cd


def nemenyi_multitest(ranks):
    """
    Note: Code extracted from Github page of STAC:
    https://github.com/citiususc/stac/blob/master/stac/nonparametric_tests.py

    Many thanks to the authors of the algorithm.

    ---
    Original documentation
    ---

    Performs a Nemenyi post-hoc test using the pivot quantities obtained by a ranking test.
    Tests the hypothesis that the ranking of each pair of groups are different.

    Parameters
    ----------
    pivots : dictionary_like
        A dictionary with format 'groupname':'pivotal quantity'

    Returns
    ----------
    Comparions : array-like
        Strings identifier of each comparison with format 'group_i vs group_j'
    Z-values : array-like
        The computed Z-value statistic for each comparison.
    p-values : array-like
        The associated p-value from the Z-distribution wich depends on the index of the comparison
    Adjusted p-values : array-like
        The associated adjusted p-values wich can be compared with a significance level

    References
    ----------
    Bonferroni-Dunn: O.J. Dunn, Multiple comparisons among means, Journal of the American Statistical Association 56
    (1961) 52–64.
    """
    k = len(ranks)
    values = list(ranks.values())
    keys = list(ranks.keys())
    versus = list(it.combinations(range(k), 2))

    comparisons = [keys[vs[0]] + " vs " + keys[vs[1]] for vs in versus]
    z_values = [abs(values[vs[0]] - values[vs[1]]) for vs in versus]
    p_values = [2 * (1 - st.norm.cdf(abs(z))) for z in z_values]
    # Sort values by p_value so that p_0 < p_1
    p_values, z_values, comparisons = map(list, zip(*sorted(zip(p_values, z_values, comparisons), key=lambda t: t[0])))
    m = int(k * (k - 1) / 2.)
    adj_p_values = [min(m * p_value, 1) for p_value in p_values]

    return comparisons, z_values, p_values, adj_p_values


def friedman_aligned_ranks_test(args):
    """
    Note: Code extracted from Github page of STAC:
    https://github.com/citiususc/stac/blob/master/stac/nonparametric_tests.py

    Many thanks to the authors of the algorithm.

    ---
    Original documentation
    ---

    Performs a Friedman aligned ranks ranking test.
    Tests the hypothesis that in a set of k dependent samples groups (where k >= 2) at least two of the groups represent
    populations with different median values.
    The difference with a friedman test is that it uses the median of each group to construct the ranking, which is
    useful when the number of samples is low.

    Parameters
    ----------
    sample1, sample2, ... : array_like
    The sample measurements for each group.

    Returns
    -------
    Chi2-value : float
    The computed Chi2-value of the test.
    p-value : float
    The associated p-value from the Chi2-distribution.
    rankings : array_like
    The ranking for each group.
    pivots : array_like
    The pivotal quantities for each group.

    References
    ----------
    J.L. Hodges, E.L. Lehmann, Ranks methods for combination of independent experiments in analysis of variance,
    Annals of Mathematical Statistics 33 (1962) 482–497.
    """
    k = len(args)
    if k < 2: raise ValueError('Less than 2 levels')
    n = len(args[0])
    if len(set([len(v) for v in args])) != 1: raise ValueError('Unequal number of samples')

    aligned_observations = []
    for i in range(n):
        loc = np.mean([col[i] for col in args])
        aligned_observations.extend([col[i] - loc for col in args])

    aligned_observations_sort = sorted(aligned_observations)

    aligned_ranks = []
    for i in range(n):
        row = []
        for j in range(k):
            v = aligned_observations[i * k + j]
            row.append(aligned_observations_sort.index(v) + 1 + (aligned_observations_sort.count(v) - 1) / 2.)
        aligned_ranks.append(row)

    rankings_avg = [np.mean([case[j] for case in aligned_ranks]) for j in range(k)]
    rankings_cmp = [r / np.sqrt(k * (n * k + 1) / 6.) for r in rankings_avg]

    r_i = [np.sum(case) for case in aligned_ranks]
    r_j = [np.sum([case[j] for case in aligned_ranks]) for j in range(k)]
    T = (k - 1) * (np.sum([v ** 2 for v in r_j]) - (k * n ** 2 / 4.) * (k * n + 1) ** 2) / float(
        ((k * n * (k * n + 1) * (2 * k * n + 1)) / 6.) - (1. / float(k)) * np.sum([v ** 2 for v in r_i]))

    p_value = 1 - st.chi2.cdf(T, k - 1)

    return T, p_value, rankings_avg, rankings_cmp


def perform_checks(results_path: str) -> pd.DataFrame:
    df = pd.read_csv(results_path, index_col=0)

    if np.any(df > 0):
        raise ValueError("Result values should be negative (the smaller the value, the better). If that's not the case,"
                         "simply flip each value signal (e.g. 0.83 -> -0.83)")

    if not isinstance(df.index.dtype, object):
        raise TypeError("First column should have datasets names")

    return df


def main(results_path: str, align: bool) -> None:
    df = perform_checks(results_path)

    n, k = df.shape
    names = df.columns  # names of methods

    # computes average ranks
    if not align:
        avranks = df.rank(axis=1).mean(axis=0).values
        cd = Orange.evaluation.scoring.compute_CD(avranks, n=n, alpha="0.05", test="nemenyi")
    else:
        T, p_value, rankings_avg, rankings_cmp = friedman_aligned_ranks_test(df.T.values.tolist())
        avranks = rankings_avg
        cd = compute_CD_for_aligned_ranks(avranks, n=n, alpha="0.05", test="nemenyi")
        # comparisons, z_values, p_values, adj_p_values = nemenyi_multitest(dict(zip(names, avranks)))

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

    parser.add_argument(
        '--align', action='store_true', required=False, default=False,
        help='Optional -- whether to align ranks or not. Will use the methodology of Friedman aligned ranks for it.'
    )

    args = parser.parse_args()
    main(results_path=args.results_path, align=args.align)
