from PySide6.QtWidgets import QMainWindow, QFileDialog

from .main_app_ui import MainAppUI
from core import (
    open_cryp_file_with_key,
    open_cryp_file,
    save_cryp_file_with_key,
    save_cryp_file,
    read_toml_string,
    write_to_toml_str,
    save_db,
    load_db,
)
from settings import (
    FILE_SETTINGS,
    FILE_SETTINGS_KEY,
)


class MainApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.load_config()

        self.main = MainAppUI(self.config['language'])
        self.setCentralWidget(self.main)
        
        # Подключаем кнопки
        self.main.open_file_b.clicked.connect(lambda: self.open_file(True))
        self.main.open_key_b.clicked.connect(lambda: self.open_file(False))

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
        save_db(self.main.way_to_file.text(), '')

    def save_db(self):
        pass

    def update_table(self):
        pass

    def open_file(self, type: bool):
        way = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files ( * )')
        if type:
            self.main.way_to_file.setText(way[0])
        else:
            self.main.way_to_key.setText(way[0])
