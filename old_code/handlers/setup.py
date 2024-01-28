from os.path import (
    exists,
)

from core import (
    get_os,
    OsException,
    ConfigException,
    read,
    write,
)


def main_check():
    os = get_os()
    data = {}
    match os:
        case 'win':
            data = win_init()
        case 'linux':
            data = linux_init()
        case 'ios':
            print('Приложение не поддерживается на IOS')
        case None:
            print('Не известная OS')
            raise OsException

    # ! Обработка ошибки файла конфига
    if not data:
        raise ConfigException

    data['os'] = os
    return data


def win_init() -> dict:
    # ! Проверка файла настроек
    from .settings import (
            win_conf_name,
            win_set_conf,
        )
    if not exists(win_conf_name):
        from core import (
            win_hide_file,
        )
        write(win_set_conf, win_conf_name)
        win_hide_file(win_conf_name)
    conf = read(win_conf_name)
    return conf


def linux_init() -> dict:
    # ! Проверка файла настроек
    from .settings import (
            lin_conf_name,
            lin_set_conf,
        )
    if not exists(lin_conf_name):
        write(lin_set_conf, lin_conf_name)
    conf = read(lin_conf_name)
    return conf
