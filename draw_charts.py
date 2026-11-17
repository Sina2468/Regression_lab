from matplotlib import use
from pandas import DataFrame
from numpy import sqrt, ceil, array
import matplotlib.pyplot as plt

use("QtAgg")


def Draw_charts(Data: DataFrame, x: list, y: list) -> None:
    col = int(ceil(sqrt(len(x))))
    row = int(ceil((len(x)) / col))

    fig, axes = plt.subplots(row, col, figsize=(5 * col, 5 * row))

    axes = array(axes).reshape(-1)

    i = 1

    for ax, _ in zip(axes, x):
        ax.scatter(Data[_], Data[y])
        ax.set_title(f"{_} : {i}")

        i += 1

    plt.show()
