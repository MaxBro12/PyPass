import pandas as pd
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem

from .main_app_ui import MainAppUI
from ..dialogs import NewKeyGenDia
from ..settings_app import SettingsApp
from core import (
    save_file_bytes,
    open_cryp_file_with_key,
    open_cryp_file,
    save_cryp_file_with_key,
    save_cryp_file,
    read_toml_string,
    write_to_toml_str,
    save_db,
    load_db,
    return_empty_bd,
    create_key,
)
from settings import (
    APP_NAME,
    MAIN_APP_SIZE,
    FILE_SETTINGS,
    FILE_SETTINGS_KEY,
    NEW_KEY_FILE,
    NEW_DB_FILE,
)
from lang import language


class MainApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.config = dict()
        self.load_config()

        self.setting_sapp = None

        self.ui = MainAppUI(self.config["language"])
        self.setCentralWidget(self.ui)
        self.setWindowTitle(APP_NAME)
        self.setMinimumSize(MAIN_APP_SIZE)

        # Подключаем кнопки
        self.ui.open_file_b.clicked.connect(lambda: self.open_file(True))
        self.ui.open_key_b.clicked.connect(lambda: self.open_file(False))

        self.ui.gen_key_b.clicked.connect(self.generate_key)
        self.ui.gen_password_b.clicked.connect(self.generate_pass)

        self.ui.add_row.clicked.connect(self.add_row)

        self.ui.open_settings_b.clicked.connect(self.open_settings)

        self.ui.table.cellChanged.connect(self.save_db)

        if self.config["save_loc"]:
            self.ui.way_to_file.setText(self.config["way_to_file"])
            self.ui.way_to_key.setText(self.config["way_to_key"])

        if self.ui.way_to_file.text() != "" and self.ui.way_to_key.text() != "":
            self.update_db()

    # Главные методы
    def load_config(self):
        self.config = read_toml_string(
            open_cryp_file_with_key(FILE_SETTINGS, FILE_SETTINGS_KEY)
        )

    def save_config(self):
        save_cryp_file_with_key(
            FILE_SETTINGS, write_to_toml_str(self.config), FILE_SETTINGS_KEY
        )

    def open_settings(self):
        self.setting_sapp = SettingsApp()
        self.setting_sapp.show()
        # exit(SetApp.exec())

    def get_db(self) -> pd.DataFrame:
        row_count = self.ui.table.rowCount()
        column_count = self.ui.table.columnCount()
        df = pd.DataFrame(index=range(row_count), columns=range(column_count))

        for row in range(row_count):
            for column in range(column_count):
                item = self.ui.table.item(row, column)
                if item is not None:
                    df.iloc[row, column] = item.text()

        return df

    def update_db(self):
        df = self.load_db()

        for col in df.columns:
            df[col] = df[col].astype("object")
        df = df.drop_duplicates()

        for i, row in enumerate(df.to_numpy()):
            if all(map(lambda x: pd.isna(x), row)):
                df = df.drop(index=i)

        self.ui.table.clear()
        self.ui.table.setRowCount(df.shape[0])
        self.ui.table.setColumnCount(df.shape[1])
        self.ui.table.setHorizontalHeaderLabels(
            language[self.config["language"]]["table_h_header"]
        )
        self.ui.table.horizontalHeader().setStretchLastSection(True)
        # self.ui.table.header.setResizeMode(QtGui.QHeaderView.ResizeToContents)
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.ui.table.setItem(i, j, item)

    def add_row(self):
        df = self.get_db()
        df.loc[len(df.index)] = language[self.config["language"]]["add_row"]
        self.save_db(df)
        self.update_db()

    def load_db(self) -> pd.DataFrame:
        return load_db(self.ui.way_to_file.text(), self.ui.way_to_key.text())

    def save_db(self, df: pd.DataFrame | None = None):
        if df is None or type(df) is int:
            df = self.get_db()
        save_db(self.ui.way_to_file.text(), df, self.ui.way_to_key.text())

    def generate_pass(self):
        pass

    def generate_key(self):
        save_file_bytes(NEW_KEY_FILE, create_key())
        save_db(
            NEW_DB_FILE,
            pd.DataFrame(
                {
                    "Name": ["New", "test"],
                    "Login": ["Password", "test"],
                    "Password": ["Data", "test"],
                }
            ),
            NEW_KEY_FILE,
        )
        dia = NewKeyGenDia(None, NEW_KEY_FILE, self.config["language"])
        dia.exec()
        self.ui.way_to_file.setText(NEW_DB_FILE)
        self.ui.way_to_key.setText(NEW_KEY_FILE)
        self.update_db()

    # ! Открытие таблицы
    def try_open(self):
        if self.ui.way_to_file.text() != "" and self.ui.way_to_key.text() != "":
            if self.config["save_loc"]:
                self.config["way_to_file"] = self.ui.way_to_file.text()
                self.config["way_to_key"] = self.ui.way_to_key.text()
                self.save_config()
            self.update_db()

    def open_file(self, type: bool):
        way = QFileDialog.getOpenFileName(self, "Open File", "", "All Files ( * )")
        if type:
            self.ui.way_to_file.setText(way[0])
            self.try_open()
        else:
            self.ui.way_to_key.setText(way[0])
            self.try_open()
