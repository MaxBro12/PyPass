from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
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

        # Выбор файла
        self.way_to_file = QLineEdit()
        self.way_to_file.setToolTip(language[lang]['way_to_file_tip'])
        self.way_to_file.setPlaceholderText(language[lang]['way_to_file_placeholder'])
        self.grid.addWidget(self.way_to_file, 0, 0, 1, 2)

        self.open_file_b = QPushButton()
        self.open_file_b.setToolTip(language[lang]['way_to_file_b'])
        self.open_file_b.setFixedSize(SMALL_BUTTOMS_SIZE)
        self.grid.addWidget(self.open_file_b, 0, 2, 1, 1)

        # Выбор ключа
        self.way_to_key = QLineEdit()
        self.way_to_key.setToolTip(language[lang]['way_to_key_tip'])
        self.way_to_key.setPlaceholderText(language[lang]['way_to_key_placeholder'])
        self.grid.addWidget(self.way_to_key, 1, 0, 1, 2)
        
        self.open_key_b = QPushButton()
        self.open_key_b.setToolTip(language[lang]['way_to_key_b'])
        self.open_key_b.setFixedSize(SMALL_BUTTOMS_SIZE)
        self.grid.addWidget(self.open_key_b, 1, 2, 1, 1)

        # Сгенерировать пароль, ключ, открыть настройки
        self.gen_key_b = QPushButton()
        self.gen_key_b.setText(language[lang]['gen_key_text'])
        self.gen_key_b.setToolTip(language[lang]['gen_key_tip'])
        self.grid.addWidget(self.gen_key_b, 2, 0, 1, 1)

        self.gen_password_b = QPushButton()
        self.gen_password_b.setText(language[lang]['gen_pass_text'])
        self.gen_password_b.setToolTip(language[lang]['gen_pass_tip'])
        self.grid.addWidget(self.gen_password_b, 2, 1, 1, 1)

        self.open_settings_b = QPushButton()
        self.open_settings_b.setToolTip(language[lang]['open_settings_b'])
        self.open_settings_b.setFixedSize(SMALL_BUTTOMS_SIZE)
        self.grid.addWidget(self.open_settings_b, 2, 2, 1, 1)

        # Таблица
        self.table = QTableView()
        self.grid.addWidget(self.table, 3, 0, 1, 3)
