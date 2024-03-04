from PySide6.QtWidgets import QMainWindow

from .main_app_ui import MainAppUI
from core import read_toml
from settings import (
    FILE_SETTINGS,
)

class MainApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # self.config = read_toml(FILE_SETTINGS)
        self.main = MainAppUI('ru')
        self.setCentralWidget(self.main)

