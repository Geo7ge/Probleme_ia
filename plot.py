import matplotlib.pyplot as plt

def plot_chart(table_sizes, solving_times, solving_times_alt):
    plt.plot(table_sizes, solving_times, label="Algo 1")
    plt.plot(table_sizes, solving_times_alt, label="Algo 2", linestyle='--')
    plt.xlabel("Complexitate")
    plt.ylabel("Timp(s)")
    # plt.xticks(range(len(table_sizes)), table_sizes)
    plt.xticks(table_sizes)
    plt.grid()
    plt.legend()
    plt.show()