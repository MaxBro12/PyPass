from sys import argv, exit

from PySide6.QtWidgets import QApplication

from client import MainApp, ErrorApp
from core import create_log, create_key
from start import main_check


app = QApplication([])


def main(args: list):
    # ? Проверка
    main_check()
    # ? Запуск приложения
    widget = MainApp()
    widget.show()
    exit(app.exec())


if __name__ == '__main__':
    try:
        main(argv)
    except Exception as err:
        create_log(err, 'crit')

        if QApplication.instance() is None:
            app = QApplication([])
        widget = ErrorApp(err)
        widget.show()
        exit(QApplication.exec())

