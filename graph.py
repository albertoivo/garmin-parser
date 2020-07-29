import matplotlib.pyplot as plt
import numpy as np


def overlay(x, y1, y2):
    fig, ax = plt.subplots(figsize=(16, 4))

    ax.plot(x, y1, color="red", marker="o")

    ax.set_xlabel("laps", fontsize=14)
    ax.set_ylabel(y1.name, color="red", fontsize=14)

    # twin object for two different y-axis on the sample plot
    ax2 = ax.twinx()

    # make a plot with different y-axis using second axis object
    ax2.plot(x, y2, color="blue", marker="o")
    ax2.set_ylabel(y2.name, color="blue", fontsize=14)

    plt.show()

    # save the plot as a file
    # fig.savefig('twinx.jpg', format='jpeg', dpi=100, bbox_inches='tight')


def overlay_hist(df):
    fig, ax = plt.subplots()
    # df.plot.hist(bins=100, alpha=0.5, range=(0, 400), ax=ax)
    df.plot.hist(bins=50, alpha=0.5, ax=ax)
    ax.legend()
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def mean(df_dropped):
    means = df_dropped.mean()
    errors = df_dropped.std()
    fig, ax = plt.subplots(figsize=(16, 4))
    means.plot.bar(yerr=errors, ax=ax)
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def overlay_timeseries(df):
    fig, ax = plt.subplots(figsize=(16, 4))
    df.plot(ax=ax)
    ax.legend()
    # plt.xlabel("Seconds")
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def heartrate(df, title=''):
    fig, ax = plt.subplots()
    df.plot(ax=ax, figsize=(16, 8))
    ax.legend()
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.title(title)
    plt.show()


def scatter(df1, df2=None):
    colors = np.random.rand(len(df1))

    if df2 is None:
        df2 = df1
        df1 = df2.index

    plt.figure(figsize=(17, 6))
    plt.scatter(x=df1, y=df2, c=colors, alpha=0.5)
    plt.gcf().autofmt_xdate()
    plt.show()


def two_scatters(df1, df2):
    x = df1
    y = df2
    z = np.sqrt(x ** 2 + y ** 2)

    plt.figure(figsize=(17, 10))

    plt.subplot(211)
    plt.scatter(x, y, s=80, c=z)

    plt.subplot(212)
    plt.scatter(x, y, s=80, c=z, marker=(5, 0))

    plt.show()
