from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QDialogButtonBox,
    QMessageBox
)

from lang import language
from settings import SETTINGS_DIA_SIZE


class NewKeyGenDia(QDialog):
    def __init__(self, parent, filename: str, lang: str) -> None:
        super().__init__(parent)
        self.setFixedSize(SETTINGS_DIA_SIZE)
        self.setWindowTitle('PyNote')

        self.col = QVBoxLayout()
        self.setLayout(self.col)

        self.label = QLabel()
        self.label.setText(language[lang]['dia_key_generated'].format(filename))
        self.col.addWidget(self.label)

        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.col.addWidget(self.buttonBox)
