from os.path import (
    exists,
)

from core import (
    get_os,
    OsException,
)


def main_check():
    os = get_os()
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

    return os


def win_init():
    from core.dirs import (
        win_hide_file,
    )
    print('Window works')


def linux_init():
    print('Linux works')


def check_settings():
    if not exists('.settings.ini'):
        txt = ''
        with open('.settings.ini', 'w') as f:
            f.write(txt)
