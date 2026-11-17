from pandas import DataFrame
from sklearn.model_selection import train_test_split
from numpy import asanyarray, ceil, linspace
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def Polynomial(Data: DataFrame, All_list: list, Chart_number: int, Degree: int) -> None:
    Score: int = 0

    while Score <= 0.75:
        train, test = train_test_split(Data, train_size=0.8)

        train_x = asanyarray(train[[All_list[Chart_number]]])
        train_y = asanyarray(train[All_list[-1]])

        test_x = asanyarray(test[[All_list[Chart_number]]])
        test_y = asanyarray(test[All_list[-1]])

        poly = PolynomialFeatures(degree=Degree)

        train_x_ = poly.fit_transform(train_x)
        test_x_ = poly.fit_transform(test_x)

        reg = LinearRegression()

        reg.fit(train_x_, train_y)

        Score = reg.score(test_x_, test_y)

    X_min = Data[[All_list[Chart_number]]].min()
    X_max = Data[[All_list[Chart_number]]].max()

    xx = linspace(X_min, X_max, 1000).reshape(-1, 1)

    xx_ = poly.fit_transform(xx)

    yy = reg.predict(xx_)

    plt.scatter(Data[All_list[Chart_number]], Data[All_list[-1]], color="blue")
    plt.plot(xx, yy, "r")
    plt.title(f"Score = {(Score * 100):.2f} %")

    plt.show()
