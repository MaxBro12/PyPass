import pandas as pd
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QTableWidgetItem
)
from PySide6.QtCore import QAbstractTableModel, Qt

from .main_app_ui import MainAppUI
from ..dialogs import NewKeyGenDia
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
    FILE_SETTINGS,
    FILE_SETTINGS_KEY,
    NEW_KEY_FILE,
    NEW_DB_FILE,
)


class PandasModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
        super().__init__()
        self.__data = data

    def rowCount(self, index):
        return self.__data.shape[0]

    def columnCount(self, index):
        return self.__data.shape[1]

    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self.__data.iloc[index.row(), index.column()])

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.__data.iloc[index.row(), index.column()] = value
            return True
        return False

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.__data.columns[section])

            if orientation == Qt.Vertical:
                return str(self.__data.index[section])

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable


class MainApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.load_config()

        self.main = MainAppUI(self.config['language'])
        self.setCentralWidget(self.main)
        
        # Подключаем кнопки

        self.main.open_file_b.clicked.connect(lambda: self.open_file(True))
        self.main.open_key_b.clicked.connect(lambda: self.open_file(False))

        self.main.gen_key_b.clicked.connect(self.generate_key)

        if self.main.open_file_b.text() != '' and self.main.open_key_b.text() != '':
            self.update_table()


    # Главные методы
    def load_config(self):
        self.config = read_toml_string(
            open_cryp_file_with_key(FILE_SETTINGS, FILE_SETTINGS_KEY)
        )

    def save_config(self):
        print('save db')
        save_cryp_file_with_key(
            FILE_SETTINGS, write_to_toml_str(self.config), FILE_SETTINGS_KEY
        )

    def load_db(self) -> pd.DataFrame:
        return load_db(self.main.way_to_file.text(), self.main.way_to_key.text())

    def save_db(self):
        pass

    def generate_key(self):
        save_file_bytes(NEW_KEY_FILE, create_key())
        save_db(NEW_DB_FILE, pd.DataFrame({'Name':['New', 'test'], 'Login':['Password', 'test'],'Password':['Data', 'test']}), NEW_KEY_FILE)
        dia = NewKeyGenDia(None, NEW_KEY_FILE, self.config['language'])
        dia.exec()
        self.main.way_to_file.setText(NEW_DB_FILE)
        self.main.way_to_key.setText(NEW_KEY_FILE)
        self.update_table()

    # ! Открытие таблицы
    def try_open(self):
        print('try to open')
        if self.main.open_file_b.text() != '' and self.main.open_file_b.text() != '':
            self.update_table

    def update_table(self):
        df = self.load_db()
        #self.main.table.setModel(PandasModel(df))
        self.main.table.setRowCount(df.shape[0])
        self.main.table.setColumnCount(df.shape[1])

        for i, row in df.iterrows():
            for j, value in row.iteritems():
                item = QTableWidgetItem(str(value))
                self.main.table.setItem(i, j, item)


    def open_file(self, type: bool):
        way = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files ( * )')
        if type:
            self.main.way_to_file.setText(way[0])
            self.try_open()
        else:
            self.main.way_to_key.setText(way[0])
            self.try_open()