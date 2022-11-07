from core import (
    ex,
    get_os,
    write,
)


class UserInp:
    def __init__(self):
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
        return 1 / 0

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
