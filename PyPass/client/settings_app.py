from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QComboBox,
    QCheckBox,
    QTextBrowser,
)
from PySide6.QtCore import QSize
from core import (
    read_toml_string,
    write_to_toml_str,
    open_cryp_file_with_key,
    save_cryp_file_with_key,
)
from settings import (
    SETTINGS_APP_NAME,
    SETTINGS_APP_SIZE,
    ALL_SPASING,
    ALL_MARGINS,
    FILE_SETTINGS,
    FILE_SETTINGS_KEY,
)
from lang import language


class SettingsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.config = read_toml_string(
            open_cryp_file_with_key(FILE_SETTINGS, FILE_SETTINGS_KEY)
        )

        # UI
        self.setWindowTitle(SETTINGS_APP_NAME)
        self.setMinimumSize(SETTINGS_APP_SIZE)

        self.grid = QGridLayout()
        self.grid.setContentsMargins(ALL_MARGINS)
        self.grid.setSpacing(ALL_SPASING)
        self.setLayout(self.grid)

        self.lang_l = QLabel()
        self.lang_l.setText(language[self.config["language"]]["set_lang"])
        self.grid.addWidget(self.lang_l, 0, 0)

        self.lang_b = QComboBox()
        for i in language.keys():
            self.lang_b.addItem(i)
        self.grid.addWidget(self.lang_b, 0, 1)

        self.save_l = QLabel()
        self.save_l.setText(language[self.config["language"]]["set_location"])
        self.grid.addWidget(self.save_l, 1, 0)

        self.save_b = QCheckBox()
        self.save_b.setToolTip(language[self.config["language"]]["set_loc_tip"])
        self.grid.addWidget(self.save_b, 1, 1)

        self.help_l = QTextBrowser()
        self.help_l.setText(language[self.config["language"]]["set_help"])
        self.grid.addWidget(self.help_l, 2, 0, 1, 2)

        # Загружаем конфиг
        self.config = dict()
        self.load_config()

        self.lang_b.setCurrentText(self.config["language"])
        if self.config["save_loc"]:
            self.save_b.toggle()

        # Соединяем
        self.lang_b.currentIndexChanged.connect(self.update_config)
        self.save_b.stateChanged.connect(self.update_config)

    def update_config(self):
        self.config["language"] = self.lang_b.currentText()
        self.config["save_loc"] = self.save_b.isChecked()

    def save_config(self):
        save_cryp_file_with_key(
            FILE_SETTINGS, write_to_toml_str(self.config), FILE_SETTINGS_KEY
        )

    def load_config(self):
        self.config = read_toml_string(
            open_cryp_file_with_key(FILE_SETTINGS, FILE_SETTINGS_KEY)
        )
