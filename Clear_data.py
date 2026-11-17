from pandas import DataFrame


def Clear_date(Data: DataFrame) -> tuple[DataFrame, list, list, list]:
    All_list = list()
    X_list = list()
    Y = list()

    for col in Data.columns:
        if Data[col].dtype == "str":
            pass

        else:
            All_list.append(col)

    for x in All_list[:-1]:
        X_list.append(x)

    Y.append(All_list[-1])

    Cleard_Data = Data[All_list]

    for col in Cleard_Data.columns:
        Cleard_Data[col] = Cleard_Data[col] / Cleard_Data[col].max()

    return Cleard_Data, All_list, X_list, Y
