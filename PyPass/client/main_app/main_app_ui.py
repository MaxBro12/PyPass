from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTableView,
)
from lang import language
from settings import ALL_MARGINS, ALL_SPASING, SMALL_BUTTOMS_SIZE


class MainAppUI(QWidget):
    def __init__(self, lang):
        super().__init__()

        self.grid = QGridLayout()
        self.grid.setSpacing(ALL_SPASING)
        self.grid.setContentsMargins(ALL_MARGINS)
        self.setLayout(self.grid)

        self.way_to_file = QLineEdit()
        self.way_to_file.setToolTip(language[lang]['way_to_file_tip'])
        self.way_to_file.setPlaceholderText(language[lang]['way_to_file_placeholder'])
        self.grid.addWidget(self.way_to_file, 0, 0)

        self.open_file_b = QPushButton()
        self.open_file_b.setToolTip(language[lang]['way_to_file_b'])
        self.open_file_b.setFixedSize(SMALL_BUTTOMS_SIZE)
        self.grid.addWidget(self.open_file_b, 0, 1)

        self.way_to_key = QLineEdit()
        self.way_to_key.setToolTip(language[lang]['way_to_key_tip'])
        self.way_to_key.setPlaceholderText(language[lang]['way_to_key_placeholder'])
        self.grid.addWidget(self.way_to_key, 1, 0)
        
        self.open_key_b= QPushButton()
        self.open_key_b.setToolTip(language[lang]['way_to_key_b'])
        self.open_key_b.setFixedSize(SMALL_BUTTOMS_SIZE)
        self.grid.addWidget(self.open_key_b, 1, 1)

        self.table = QTableView()
        self.grid.addWidget(self.table, 2, 0, 1, 2)
