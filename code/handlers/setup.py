from os.path import (
    exists,
)

from tools import (
    get_os,
    OsException,
    create_file,
)


def main_check():
    os = get_os
    match os:
        case 'win':
            win_init()
        case 'linux':
            linux_init()
        case 'ios':
            print('Приложение не поддерживается на IOS')
        case None:
            print('Не известная OS')
            raise OsException


def win_init():
    pass


def linux_init():
    pass


def check_settings():
    if not exists('.settings.ini'):
        txt = ''
        with open('.settings.ini', 'w') as f:
            f.write(txt)
