from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon


from settings import WARNING_APP_ICON


class WarningApp(QDialog):
    def __init__(self, msg) -> None:
        super().__init__()
        # ? Окно
        self.setWindowTitle('Warning!')
        self.setWindowIcon(QIcon(WARNING_APP_ICON))
        self.setBaseSize(QSize(200, 60))

        # ! Разметка
        self.row = QVBoxLayout()
        self.row.setContentsMargins(5, 5, 5, 5)
        self.row.setSpacing(5)
        self.row.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.row)

        self.text = QLabel()
        self.text.setText(msg)
        self.row.addWidget(self.text)

        self.button = QPushButton()
        self.button.setFixedSize(QSize(100, 25))
        self.button.setText('OK')
        self.button.clicked.connect(self.close())
        self.row.addWidget(self.button)
