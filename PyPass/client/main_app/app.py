from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
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
)



class PandasModel(QAbstractTableModel):
    def __init__(self, df, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = df

    def rowCount(self, parent=None):
        return len(self._dataframe.index)

    def columnCount(self, parent=None):
        return len(self._dataframe.columns)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._dataframe.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._dataframe.columns[col]
        return None


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
        save_cryp_file_with_key(
            FILE_SETTINGS, write_to_toml_str(self.config), FILE_SETTINGS_KEY
        )

    def load_db(self):
        load_db(self.main.way_to_file.text(), self.main.way_to_key.text())

    def save_db(self):
        pass

    def generate_key(self):
        save_file_bytes(NEW_KEY_FILE, create_key())
        dia = NewKeyGenDia(None, NEW_KEY_FILE, self.config['language'])
        dia.exec()

    # ! Открытие таблицы
    def try_open(self):
        print('try to open')
        if self.main.open_file_b.text() != '' and self.main.open_file_b.text() != '':
            self.update_table

    def update_table(self):
        df = self.load_db()
        self.main.table.setModel(PandasModel(df))
    
    def open_file(self, type: bool):
        way = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files ( * )')
        if type:
            self.main.way_to_file.setText(way[0])
            self.try_open()
        else:
            self.main.way_to_key.setText(way[0])
            self.try_open()