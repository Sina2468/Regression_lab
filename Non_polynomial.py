from pandas import DataFrame
from numpy import sin, log, ceil, sqrt, array
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from os import system


def Model_1(x, a, b, c, d, e) -> int:
    y = (a * x + b) / (c * x + d) + e
    return y


def Model_2(x, a, b, c, d, e, f) -> int:
    y = e * ((a * x + b) ** (1 / d)) + f
    return y


def Model_3(x, a, b, c, d) -> int:
    y = c * abs(a * x + b) + d
    return y


def Model_4(x, a, b, c, d) -> int:
    y = c * sin(a * x + b) + d
    return y


def Model_5(x, a, b, c, d, e):
    y = d * (c ** (a * x + b))
    return y


def Model_6(x, a, b, c, d, e):
    y = d * (log(c, a * x + b)) + e
    return y


def Model_7(x, a, b, c, d, e, f, h):
    y = f / (d * (c ** (a * x + b)) + e) + h
    return y


def Non_polynomial(Data: DataFrame, All_list: list, Chart_number: int) -> None:
    Models = [
        Model_1,
        Model_2,
        Model_3,
        Model_4,
        Model_5,
        Model_6,
        Model_7,
    ]

    col = int(ceil(sqrt(len(Models))))
    row = int(ceil(len(Models) / col))

    fig, axes = plt.subplots(row, col, figsize=(5 * col, 5 * row))

    axes = array(axes).reshape(-1)

    i = 1

    Scores: dict = {}

    for Model, ax in zip(Models, axes):
        popt = curve_fit(
            Model,
            Data[All_list[Chart_number]].values,
            Data[All_list[-1]].values,
            maxfev=1000000,
        )[0]

        ax.scatter(Data[All_list[Chart_number]], Data[All_list[-1]])
        ax.plot(
            Data[All_list[Chart_number]],
            Model(Data[All_list[Chart_number]], *popt),
            "r",
        )

        R2 = r2_score(Data[All_list[-1]], Model(Data[All_list[Chart_number]], *popt))
        Scores[i] = R2

        ax.set_title(f"{i} , Score = {(R2 * 100):.2f} %")

        i += 1

    Best_chart = list(Scores.values()).index(max(Scores.values())) + 1

    system("cls|clear")

    print(f"""=================================================
    
The best chart is >>> {Best_chart}

=================================================""")

    plt.show()
