from Open_file import Open_file
from Clear_data import Clear_date
from draw_charts import Draw_charts
from os import system
from Menu import Menu_1, Menu_2
from Polynomial import Polynomial
from Non_polynomial import Non_polynomial


def Main() -> None:

    while True:
        system("cls|clear")

        Data_frame = Open_file(str(input("File name >>> ")))

        Clear_date_frame, All_list, X_list, Y = Clear_date(Data_frame)

        Draw_charts(Clear_date_frame, X_list, Y)

        system("cls|clear")

        Chart_number = Menu_1(X_list)

        system("cls|clear")

        Type, Degree = Menu_2()

        if Type == 1:
            Polynomial(Clear_date_frame, All_list, Chart_number, Degree)

        elif Type == 2:
            Non_polynomial(Clear_date_frame, All_list, Chart_number)

        else:
            break


if __name__ == "__main__":
    Main()
