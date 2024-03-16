from typing import Final
from PySide6.QtCore import QSize, QMargins


# ! ОСНОВА
ERROR_FOUND: Final = 'Найдена критическая ошибка! Отправьте файл "logger.log" разработчику'

FILE_SETTINGS: Final = 'settings.toml'
FILE_SETTINGS_KEY: Final = b'o_yl3RRwxwQCAqBlCncJR--fzxFxdrGV6aDqdqXH8yM='
SETTINGS_IN: Final = {
    'language': 'ru',
    'save_loc': True,
    'way_to_file': '',
    'way_to_key': '',
}
NEW_KEY_FILE: Final = 'PyPassKey.pypass'
NEW_DB_FILE: Final = 'Pandas.pypass'


# ! ОКНА
MAIN_APP_SIZE: Final = QSize(700, 500)
ERROR_APP_SIZE: Final = QSize(200, 50)
WARNING_APP_SIZE: Final = QSize(200, 50)

ALL_SPASING: Final = 2
ALL_MARGINS: Final = QMargins(2, 2, 2, 2)

SMALL_BUTTOMS_SIZE: Final = QSize(30, 30)

SETTINGS_DIA_SIZE: Final = QSize(400, 150)
