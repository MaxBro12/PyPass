import pandas as pd
from io import StringIO
from .cryp import save_cryp_file, open_cryp_file


def return_empty_bd() -> pd.DataFrame:
    return pd.DataFrame()


def save_db(way: str, db: pd.DataFrame, way_to_key: str):
    save_cryp_file(way, db.to_string(), way_to_key)


def load_db(way: str, way_to_key: str):
    return pd.read_csv(StringIO(open_cryp_file(way, way_to_key)), sep=',')

