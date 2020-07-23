import matplotlib.pyplot as plt


def get_sec(time_str):
    """Get Seconds from time."""
    if (len(time_str)) == 5:
        time_str = '00:' + time_str
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def overlay_graph(x, y1, y2):
    fig, ax = plt.subplots(figsize=(16, 4))

    ax.plot(x, y1, color="red", marker="o")

    ax.set_xlabel("laps", fontsize=14)
    ax.set_ylabel(y1.name, color="red", fontsize=14)

    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()

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


def mean_graph(df_dropped):
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
