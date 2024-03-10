from PySide6.QtWidgets import QMainWindow

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
        self.main

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
        pass

    def save_db(self):
        pass

    def update_table(self):
        pass

