from .lang import (
    ru,
    en,
)
from .excep import (
    KillException,
)


emp_conf = {
    'debug': True,
    'lang': 'ru',
}


class UserInp:
    def __init__(self, config: dict = emp_conf):
        # ? Загружаем конфиг файл в формате словаря
        self.config = config

        # ? Загружаем языковую базу
        self.lang = None
        match self.config['lang']:
            case 'ru':
                self.lang = ru
            case 'en':
                self.lang = en
            case _:
                self.lang = ru

        # ? Настройки запуска
        self.progrun = False

        # ? Список команд
        self.commands = {
            'admin': self.admin,
            'help': self.help,
            'stop': self.stop,
            'hello': self.hello,
        }

    def run(self):
        self.progrun = True

        # ! Вывод приветстренного сообщения
        self.start_message()

        # ! Главный цикл программы
        while self.progrun:
            self.user_input()

    def start_message(self):
        print(self.lang['startm'])

    def help_message(self):
        print(
            self.lang['helpm']
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
            print(f'{self.lang["uncom"]}"{com}"')

    def help(self, adt=None):
        '''Use 'help' command if '''
        if adt is None:
            self.help_message()
        elif adt[0] in ('list', 'l'):
            print(adt[0])
            print('List of all commands:')
            for command in self.commands:
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
        '''Stopping user input'''
        self.progrun = False

    def admin(self, args: list):
        match args[0]:
            case 'kill':
                raise KillException

    # ? =============== Функции =================
    '''
    Для стабильной работы команда (она же является методом класса) должна:
    1) Иметь документацию. Именно она выписывается как описание
    с использованием команды help
    2) print - команды должны что-то выводить
    3) args - аргументы в функции передаются одним списком
    Пример:
    Команда - help hello в виде интерпретатора выглядит
    как метод help с единственным аргументом ['hello'] являющимся списком
    Разделяется все пробелом:
    help hello stop = self.help(self, ['hello', 'stop'])
    Так же все что передается в аргумент является строкой!
    4) Все команды должны быть в словаре self.commands:
    ключ - слово как обращаться к функции
    значение - метод
    5) Названия команд не должны иметь в названии:
    - пробел
    - специальные символы, не все консоли могут их поддерживать
    Рекомендуется для ввода использовать стандартные латинские символа,
    вывод же может быть любым языком.
    '''

    def hello(self, args):
        print(f'Hello, world! {args[0]}')
