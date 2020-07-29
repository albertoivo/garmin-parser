import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def get_number(df):
    log_returns = np.log(df / df.shift(1))
    return log_returns.corr()


def heatmap(correlacao):
    sns.set()

    f, ax = plt.subplots(figsize=(10, 6))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    mask = np.zeros_like(correlacao, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    sns.heatmap(correlacao, mask=mask, cmap=cmap, vmax=1, center=0.5,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

