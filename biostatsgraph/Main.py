import pandas as pd
import pandas.core.frame
from matplotlib import pyplot as plt


def display_graph(data: pandas.core.frame.DataFrame):
    heights_str = "Height (in)"
    weights_str = "Weight (lbs)"

    heights = data[heights_str].tolist()
    weights = data[weights_str].tolist()

    plt.scatter(heights, weights, color="#ff0000")
    plt.title("A scatter graph of height by weight")

    plt.xlabel(heights_str)
    plt.ylabel(weights_str)

    plt.show()


def main():
    data = pd.read_csv("biostats.csv")
    display_graph(data)


if __name__ == "__main__":
    main()
