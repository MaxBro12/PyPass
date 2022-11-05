from os import (
    mkdir,
)
from os.path import (
    join,
    exists,
)
from win32con import (
    FILE_ATTRIBUTE_HIDDEN,
)
from win32api import (
    SetFileAttributes,
)


def create_folder(name: str, way: str = None) -> bool:
    """
    Создает папку по пути way с именем name.
    Если указать путь вместе с названием папки в параметре name,
    переменная way = None.
    Возвращает True или False в зависимости от исхода операции.
    """
    try:
        # ? Проверка создания пустого названия
        if name == '':
            raise ValueError
        # ? Если путь передан в название файла
        if way is None:
            way = name
        else:
            way = join(way, name)

        # ! Создание
        mkdir(way)
        return True
    except FileExistsError:
        print(f'Папка {name} уже существует!')
        return False
    except FileNotFoundError:
        print(f'Ошибка в пути, проверьте путь {way}')
        return False
    except ValueError:
        print(f'Попытка создать папку без названия! "{name}" {way}')


def create_file(
    name: str,
    way: str = None,
    inner_text: str = None
) -> bool:
    """
    Создает файл с названием и расширением, указанным в name,
    по пути way, так же записывает в нутрь текст innet_text.
    Если указать путь вместе с названием папки в параметре name,
    переменная way = None.
    Возвращает True или False в зависимости от исхода операции.
    """
    try:
        # ? Проверяем расширение файла
        if len(name.split('.')) == 1:
            raise ValueError

        # ? Если путь передан в название файла
        if way is None:
            way = name
        else:
            way = join(way, name)

        # ? Защита от перезаписи существующих файлов
        if exists(way):
            raise FileExistsError

        # ! Создание
        with open(way, 'w') as f:
            if inner_text is not None:
                f.write(inner_text)
            f.close()
        return True
    except FileExistsError:
        print(f'Файл {name} уже существует!')
        return False
    except FileNotFoundError:
        print(f'Ошибка в пути, проверьте путь {way}')
        return False
    except ValueError:
        print(f'Попытка создать файл без расширения: {way}')
        return False


def load_file(name: str):
    try:
        with open(name, 'r') as f:
            return f
    except FileNotFoundError:
        return None


def win_hide_file(name: str):
    try:
        SetFileAttributes(name, FILE_ATTRIBUTE_HIDDEN)
        return True
    except FileNotFoundError:
        return False
    else:
        return False
