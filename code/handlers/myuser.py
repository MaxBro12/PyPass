from core import (
    UserInp,
    waymaker,
    load_b_file,
    write_to_cb,
)
from cryp import (
    create_key,
    load_key,
    save_key,
    encrypt,
    decrypt,
    passinp,
)

from os.path import (
    exists,
)
from os import (
    makedirs,
    path,
    listdir,
    remove,
)


class Program(UserInp):
    def __init__(self, config: dict = ..., args: list = None):
        super().__init__(config, args)
        self.adt_commands = {
            'init': self.initbase,
            'add': self.add,
            'remove': self.remove,
            'list': self.list,
            'view': self.view,
        }
        self.commands.update(self.adt_commands)

    # ? Программные
    def save_key_com(self, key, way):
        save_key(key, path.join(way, 'pypass.key'))

    def not_exict_check(self, msg: str):
        while True:
            way = input(msg + '\n')
            if not exists(way):
                print(f"{self.lang['necf']}{way}{self.lang['necs']}")
                if input(self.lang['necA']) in self.confirm:
                    continue
                else:
                    return False
            break
        return way

    def exict_check(self, msg: str):
        while True:
            way = input(msg + '\n')
            if exists(way):
                print(f"{self.lang['excf']}{way}")
                if input(self.lang['excA']) in self.confirm:
                    continue
            else:
                return way
                break

    # ! ОСНОВНЫЕ
    def initbase(self):
        """Инизиализирует базу паролей"""
        key = bytes()
        new_data = []

        # ! Создание ключа
        print(self.lang['havekey'])
        keyq = input(self.lang['havekeyA'])
        if keyq in self.confirm:
            pass
        else:
            while True:
                # ? Предлагаем ключ
                try_key = create_key()
                print(f"{self.lang['genkey']}{try_key}\n")
                ans = input(self.lang['genkeyA'])

                # ? Подтверждаем ключ или новый
                if ans in self.confirm:
                    key = try_key
                    break
                elif ans in self.reject:
                    continue

        # ! Сохранение ключа
        inp = input(self.lang['savekeyA'])
        if inp in self.confirm:
            way = input(self.lang['waytokey'])
            if not exists(way):
                print(self.lang['waynotexis'] + way)
                inp = input(self.lang['waynotexisA'])
                if inp in self.confirm:
                    makedirs(way)
                    self.save_key_com(key, way)
                elif inp in self.reject:
                    self.save_key_com(key, '')
                    print(self.lang['savekeyHere'])
            else:
                self.save_key_com(key, way)

            # ? Скрыть ключ
            if input(self.lang['hidekey']) in self.confirm:
                if self.os == 'win':
                    from core import win_hide_file
                    win_hide_file(path.join(way, 'pypass.key'))
                elif self.os == 'linux':
                    from core import lin_hide_file
                    lin_hide_file(path.join(way, 'pypass.key'))

            # * Запоминаем где лежит ключ
            self.config['key'] = path.join(way, 'pypass.key')

        elif inp in self.reject and keyq in self.reject:
            self.save_key_com(key, '')
            print(self.lang['savekeyHere'])

        # ! Создание базы паролей
        while True:
            wayp = input(self.lang['waytopass'])
            if not exists(wayp):
                print(self.lang['waynotexis'] + wayp)
                inp = input(self.lang['waynotexisA'])
                if inp in self.confirm:
                    makedirs(wayp)
                    break
            else:
                if len(listdir()) > 0:
                    if input(self.lang['waynotempty']) in self.confirm:
                        break

        # * Запоминаем где лежит папка
        self.config['base'] = str(wayp)

        # ? Скрываем папку с паролями
        if self.config['os'] == 'win':
            from core import win_hide_file
            win_hide_file(wayp)
        elif self.config['os'] == 'linux':
            from core import lin_hide_file
            lin_hide_file(wayp)

        # ! Сохраняем в конфиг
        if self.config['os'] == 'win':
            from core import win_hide_file, win_show_file
            from .settings import win_conf_name
            win_show_file(win_conf_name)
            self.update_conf()
            win_hide_file(win_conf_name)
        elif self.config['os'] == 'linux':
            self.update_conf()
        print(self.lang['allisready'])

    def delete(self):
        """Удаляет базу паролей и приложения"""
        pass

    # ? Основное ==============================================================
    def create_pass(self, args: list = None):
        pass

    def load_key(self, args: list = None):
        """Загрузить ключ"""
        way = ''
        if args is None:
            way = self.not_exict_check(self.lang['loadkey'])
        else:
            way = args[0]
        self.config['key'] = way

    def add(self, args: list = None):
        """Добавляет в базу пароль по введенным меткам"""
        # ? Загрузаем ключ если его нет
        if self.config['key'] == '':
            self.load_key()
        # ? Получаем метки, если они не переданы в метод
        if args is None:
            args = input(self.lang['addf'])
            args = args.split(' ')
        args[-1] = args[-1] + '.txt'
        args = [self.config['base'], *args]

        # ! Скрытый ввод пароля и сохранение
        passw = passinp(self.lang['passinp'])
        waymaker(args, encrypt(passw, load_key(self.config['key'])))

    def remove(self, args: list = None):
        """Удаляет пароль по введенным меткам"""
        if args is None:
            args = input(self.lang['rmf'])
            args = args.split(' ')
        args[-1] = args[-1] + '.txt'
        args = [self.data[1], *args]
        args = path.join(*args)

        if input(self.lang['rmA']) in self.confirm:
            remove(args)
        else:
            print(self.lang['rmR'])

    def list(self):
        """Выводит список всех сохраненых меток"""
        if self.config['os'] == 'win':
            from core import win_wayfinder
            dirs = win_wayfinder(self.config['base'])
        elif self.config['os'] == 'linux':
            from core import lin_wayfinder
            dirs = lin_wayfinder(self.config['base'])

        # ? Вывод
        print(self.lang['lstF'])
        for i in dirs:
            i = ' '.join(i)
            print(i)

    def view(self, args: list = None):
        """Выводит запрошенный пароль, а так же копирует это в буфер обмена"""
        if args is None:
            args = input(self.lang['rmf'])
            args = args.split(' ')
        args[-1] = args[-1] + '.txt'
        args = [self.config['base'], *args]
        args = path.join(*args)

        if self.config['key'] == '':
            self.load_key()

        print(write_to_cb(
            decrypt(load_b_file(args), load_key(self.config['key']))
        ))
