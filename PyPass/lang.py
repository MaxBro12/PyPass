from typing import TypedDict


class Lang(TypedDict):
    ru: dict
    eng: dict


language = {
    'ru': {
        'way_to_file_placeholder': 'Путь к файлу',
        'way_to_file_tip': 'Введите путь до файла',
        'way_to_file_b': 'Выберете файл',

        'way_to_key_placeholder': 'Путь к ключу',
        'way_to_key_tip': 'Введите путь до ключа',
        'way_to_key_b': 'Выберете ключ',

        'gen_pass_text': 'Создать пароль',
        'gen_pass_tip': 'Создает пароль и копирует его в буфер обмена',
        'gen_key_text': 'Создать ключ',
        'gen_key_tip': 'Если у вас нет ключа, создает его и созраняет в рабочую директорию приложения', 
        'open_settings_b': 'Открыть настройки',

        'table_tip': 'Ваши пароли',

        'dia_cant_decode_file': 'Файл не возможно декодировать этим ключем',
        'dia_cant_find_file': 'По введенному пути не найдено файлов',
    },
    'eng': {

    },
}
