def log_graphs(probabilities_path):
    """
    Plots probability graphs to files, one file per graph
    :param probabilities_path:
    :return:
    """
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.cm import viridis
    from matplotlib.colors import to_hex
    import os

    dfb = pd.read_csv(os.path.join(probabilities_path, 'probabilities.csv'))
    variables = np.unique(['_'.join(y.split('_')[:-1]) for y in [x for x in dfb.columns if 'fitness' not in x]])

    _fitness = dfb['fitness_mean']

    ''' Creates one plot per variable '''
    for variable_name in variables:
        plt.clf()
        ax = plt.subplot()

        try:
            if (variable_name + '_scale' in dfb.columns) and (variable_name + '_loc' in dfb.columns):
                raw = [variable_name + '_' + x for x in ['loc', 'scale']]
            else:  # is continuous
                raw = [x for x in dfb.columns if variable_name in x]
        except TypeError as te:
            continue

        values = dfb.loc[:, raw]

        colors = [to_hex(x) for x in viridis(np.linspace(0, 1, len(values.columns) + 1))]

        ax.set_title(variable_name)
        last_bottom = np.zeros(len(values))
        x_axis = np.arange(len(values))
        width = 0.98
        bars = []
        labels = []
        for i, val_name in enumerate(values.columns):
            bars += [plt.bar(x_axis, values[val_name], bottom=last_bottom, width=width, color=colors[i])]
            labels += [val_name.split('_')[-1]]
            last_bottom += values[val_name]

        bars += [ax.plot(_fitness, label='avg fitness', c=colors[-1])[0]]
        labels += ['avg fitness']

        ax.set_xlabel('generation')
        ax.set_ylabel('probability')

        # puts legend outside plot
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.2, box.width, box.height * 0.8])

        ax.legend(
            tuple(bars), tuple(labels), loc='upper center',
            bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=3
        )

        plt.savefig(
            os.path.join(probabilities_path, 'probs_%s.pdf' % variable_name)
        )


if __name__ == '__main__':
	log_graphs('/A/henry/pbil/metadata/pbil_holdout/metadata/2021-08-30-16-47-37/23517/sample_05_fold_00')