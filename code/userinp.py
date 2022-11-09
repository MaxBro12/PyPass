from os import (
    mkdir,
)
from os.path import (
    exists,
    join,
)

from core import (
    ex,
    get_os,
    write,
    save_f_list,
    not_exict_check,
    exict_check,
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
        inp = input('У вас есть ключ? [Y - да / n - нет]\n')
        if inp == 'n':
            while True:
                try_key = create_key()
                print(f'Предлагаю ключ:\n{try_key}\n')
                ans = input('Оставляем таким [Y] или создать новый [n]\n')
                if ans == 'Y':
                    key = try_key
                    del try_key
                    break
                elif ans == 'n':
                    continue

        # ! Сохранение ключа
        inp = input(
            'Приложению сохранить ключ? [Y - да / n - нет]\n' +
            'Рекомендуется НЕ сохранять данные по расположению ключа\n'
        )
        if inp == 'Y':
            way = not_exict_check('Введите путь, где сохранить папку:')
            if not way:
                return None
            folder = exict_check('Введите название папки, где сохранить ключ:')
            if not folder:
                return None
            way = join(way, folder)
            mkdir(way)
            if self.os == 'win':
                from core.mypywindow import win_hide_file
                win_hide_file(way)
                with open(join(way, 'pypass.key'), 'wb') as f:
                    f.write(key)
                del key
            elif self.os == 'linux':
                # TODO: НЕ РАБОТАЕТ!!!
                return False
                from core.mypylinux import lin_hide_file
                lin_hide_file(way)
            self.data[0] = way
        elif inp == 'n':
            with open('pypass.key', 'wb') as f:
                f.write(key)
            del key
            print(
                'Файл сохранен в директории с приложением "pypass.key"' +
                'ОБЯЗАТЕЛЬНО! Переместите его в другую директорию или флешку'
            )

        # ! Создание базы паролей
        way = not_exict_check('Введите путь где сохранить базу паролей:\n')
        if not way:
            return None
        folder = exict_check(
            'Введите название папки' +
            'Внимание! Папка будет скрыта для обычных пользователей'
        )
        if not folder:
            return None
        way = join(way, folder)
        mkdir(way)
        if self.os == 'win':
            from core.mypywindow import win_hide_file
            win_hide_file(way)
        elif self.os == 'linux':
            # TODO: НЕ РАБОТАЕТ!!!
            return False
            from core.mypylinux import lin_hide_file
            lin_hide_file(way)
        self.data[1] = way
        if self.os == 'win':
            from core.mypywindow import win_hide_file, win_show_file
            from handlers.settings import win_conf_name
            win_show_file(win_conf_name)
            save_f_list(win_conf_name, self.data)
            win_hide_file(win_conf_name)
        elif self.os == 'linux':
            from core.mypylinux import lin_hide_file  # , win_show_file
            from handlers.settings import lin_conf_name
            # win_show_file(lin_conf_name)
            save_f_list(lin_conf_name, self.data)
            win_hide_file(lin_conf_name)
        print('Все готово! Добавьте пароль через команду "add"')

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
