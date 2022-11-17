from os import (
    mkdir,
    makedirs,
    walk
)
from os.path import (
    join,
    exists,
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


# ! Работа с файлами через список
def load_f_list(name: str, clean: bool = True) -> list:
    try:
        with open(name, 'r') as f:
            data = f.readlines()
        if clean:
            data = list(map(lambda x: x.replace('\n', ''), data))
        return data
    except FileNotFoundError:
        print(f'Ошибка в пути файла {name}')
        return False


def save_f_list(name: str, data: list) -> bool:
    try:
        with open(name, 'w') as f:
            data = '\n'.join(data)
            f.write(data)
        return True
    except FileNotFoundError:
        print(f'Ошибка в пути файла {name}')
        return False


def load_b_file(way: str):
    return open(way, 'rb').read()


# ! Обработчики стандартных библиотек
def not_exict_check(msg: str):
    while True:
        way = input(msg + '\n')
        if not exists(way):
            print(f'Путь не найден.\n{way}\nПроверьте путь!')
            if input('Попробовать еще раз? [Y - n]\n') == 'Y':
                continue
            else:
                return False
        break
    return way


def exict_check(msg: str):
    while True:
        way = input(msg + '\n')
        if exists(way):
            print(f'Путь уже существует.\n{way}')
            if input('Попробовать еще раз? [Y - n]\n') == 'Y':
                continue
        else:
            return way
            break


def waymaker(args: list, content):
    """Создает директорию и файл в режиме 'wb'"""
    print(args)
    way = join(*args[:-1])
    print(way)
    if not exists(way):
        makedirs(way)
    with open(join(way, args[-1]), 'wb') as f:
        f.write(content)
