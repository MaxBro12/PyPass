import pandas as pd
from io import StringIO
from .cryp import save_cryp_file, open_cryp_file

from PySide6.QtWidgets import QTableWidget
from PySide6.QtCore import Signal


class PandasIntegrationTable(QTableWidget):
    dataChanged = Signal()

    def __init__(self):
        super().__init__()
        self.__data = pd.DataFrame()


def return_empty_bd() -> pd.DataFrame:
    return pd.DataFrame()


def save_db(way: str, db: pd.DataFrame, way_to_key: str):
    # df = db.to_csv("pandas.csv", index=False)
    # with open('pandas.txt', 'w') as f:
    #    f.write(df)

    # with open('pandas.txt', 'w') as f:
    #    f.write(db.to_string())

    save_cryp_file(way, db.to_csv(index=False, header=False), way_to_key)


def load_db(way: str, way_to_key: str):
    # return pd.read_csv("pandas.csv")
    # with open('pandas.txt', 'r') as f:
    #    return pd.read_csv(StringIO(f.read()), sep=',')
    return pd.read_csv(
        StringIO(open_cryp_file(way, way_to_key)),
        sep=",",
        names=("header", "login", "pass"),
        dtype={"header": "object", "login": "object", "pass": "object"},
    )
