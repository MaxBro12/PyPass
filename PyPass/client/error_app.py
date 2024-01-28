from PySide6.QtWidgets import QDialog, QLabel, QTextEdit, QVBoxLayout
from PySide6.QtCore import QSize

from settings import ERROR_FOUND


class ErrorApp(QDialog):
    def __init__(self, msg: str | Exception):
        super().__init__()
        # ? Окно
        self.setWindowTitle('ERROR')
        self.setBaseSize(QSize(200, 150))

        # ? Разметка
        self.col = QVBoxLayout()
        self.col.setContentsMargins(5, 5, 5, 5)
        self.col.setSpacing(5)
        self.setLayout(self.col)

        # ? Виджеты
        self.error_found = QLabel()
        self.error_found.setText(ERROR_FOUND)
        self.col.addWidget(self.error_found)

        self.error_log = QTextEdit()
        self.error_log.setText(str(msg))
        self.col.addWidget(self.error_log)
