from os.path import (
    exists,
)

from core import (
    get_os,
    OsException,
    ConfigException,
    create_file,
    load_f_list,
)


def main_check():
    os = get_os()
    data = []
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
    return os, data


def win_init():
    # ! Проверка файла настроек
    from .settings import (
            win_conf_name,
            win_set_conf,
        )
    if not exists(win_conf_name):
        from core.mypywindow import (
            win_hide_file,
        )
        create_file(win_conf_name, inner_text=win_set_conf)
        win_hide_file(win_conf_name)
    conf = load_f_list(win_conf_name)
    return conf


def linux_init():
    # ! Проверка файла настроек
    from .settings import (
            lin_conf_name,
            lin_set_conf,
        )
    if not exists(lin_conf_name):
        create_file(lin_conf_name, inner_text=lin_set_conf)
    conf = load_f_list(lin_conf_name)
    return conf
