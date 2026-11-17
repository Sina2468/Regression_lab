from pandas import DataFrame, read_csv
from sys import exit


def Open_file(file_name: str) -> DataFrame:
    try:
        return read_csv(file_name)
    except:
        input("Can't open this file :(\n\nPress any key to exit ... ")
        exit()
