from os.path import (
    exists,
)
from core import (
    ex,
    get_os,
    write,
)
from cryp import (
    create_key,
)


class UserInp:
    def __init__(self, os, data):
        self.bug_rep = True
        self.progrun = False
        self.commands = {
            'pypass': self.pypass,
            'help': self.help,
            'stop': self.stop,
            'init': self.init,
            'delete': self.delete,
            'add': self.add,
            'remove': self.remove,
            'list': self.list,
            'view': self.view,
            'newpass': self.create_pass,
        }

        self.os = os
        self.data = data

    def run(self):
        self.progrun = True

        # ! Вывод приветстренного сообщения
        self.start_message()

        # ! Главный цикл программы
        while self.progrun:
            self.user_input()

    def start_message(self):
        print('Use "help" command for more info')

    def help_message(self):
        print(
            'Hi! This app is using my consol engine.\n' +
            'Use "help list" (or "l") for show all commands' +
            ' or "help and name of command" for info about command'
        )

    def user_input(self):
        '''
        Метод пользовательского ввода.
        Запускает набранную команду из списка команд.
        '''
        word = str(input(': ')).split()
        com = word[0]
        if com in self.commands:
            command = self.commands[com]
            try:
                if len(word) > 1:
                    addition = word[1::]
                    return command(addition)
                else:
                    return command()
            except TypeError as error:
                print('Wrong command!')
                if self.bug_rep:
                    print(error)
                self.user_input()
        else:
            print(f'Unknown command: "{com}"')

    def help(self, adt=None):
        '''Use 'help' command if '''
        if adt is None:
            self.help_message()
        elif adt[0] in ('list', 'l'):
            print(adt[0])
            print('List of all commands:')
            for command in self.commands:
                if command == 'pypass':
                    continue
                print(f'\t{command} - {self.commands[command].__doc__}')
        else:
            for com in adt:
                try:
                    com = str(com)
                    if com in self.commands:
                        print(f'Docs {com}:\n\t{self.commands[com].__doc__}')
                    else:
                        print(f'Unknown command {com}, use "help l" command')
                except Exception as error:
                    print(error)
                    self.user_input()

    def stop(self):
        """Правильно закрывает приложение.
        Рекомендуется закрывать приложение именно через эту команду!"""
        self.progrun = False

    def pypass(self, args: list):
        match args[0]:
            case 'kill':
                raise ex
            case 'os':
                print(get_os())
            case 'copy':
                write('Hello fuckers!')

    # ! Главное ===============================================================
    def init(self):
        """Инизиализирует базу паролей"""
        key = bytes()
        new_data = []

        # ! Создание ключа
        print('Для шифрования данных требуется ключ шифрования.')
        inp = input('Он у вас есть? [Y - да / n - нет]')
        if inp == 'n':
            while True:
                try_key = create_key()
                print(
                    f'Предлагаю ключ:\n{key}\n'
                )
                gener = input(
                    'Оставляем таким [Y], сгенерировать новый [n]' +
                    'или выйти режима создания [STOP]?'
                )
                if gener == 'Y':
                    key = try_key
                    break
                elif gener == 'n':
                    continue
                elif gener == 'STOP':
                    return None
        inp = input(
            'Приложению сохранять клуч?' +
            'Рекомендуется НЕ сохранять данные по расположению ключа,' +
            'но при дальнейшем использовании придется самостоятельно' +
            'указывать расположения файла с ключем.\n' +
            '[Y / n]\n'
        )
        if inp == 'Y':
            while True:
                way = input('Введите место хранения ключа:\n')
                if not exists(way):
                    print('Такого пути не существует')
                    continue
                else:
                    break
            fold = input('Введите название папки, где будет храниться ключ:\n')
            # TODO: Доделать отслеживание ошибки
        elif inp == 'n':
            with open('pypass.key', 'wb') as f:
                f.write(key)
            del key
            print(
                'Файл сохранен в директории с приложением "pypass.key"' +
                'ОБЯЗАТЕЛЬНО! Переместите его в другую директорию или флешку'
            )

        # ! Создание базы паролей
        inp = input('Введите путь где сохранить базу паролей:\n')
        fold = input(
            'Введите название папки' +
            'Внимание! Папка будет скрыта для обычных пользователей'
        )

    def delete(self):
        """Удаляет базу паролей и приложения"""
        pass

    # ? Основное ==============================================================
    def create_pass(self, args: list = None):
        pass

    def add(self):
        """Добавляет в базу """
        pass

    def remove(self):
        pass

    def list(self):
        pass

    def view(self):
        pass
