from core import (
    UserInp,
)
from crypt import (
    create_key,
    load_key,
    save_key,
    encrypt,
    decrypt,
    passinp,
)


class Program(UserInp):
    def __init__(self, config: dict = ..., args: list = None):
        super().__init__(config, args)

    def init(self):
        """Инизиализирует базу паролей"""
        key = bytes()
        new_data = []

        # ! Создание ключа
        print(self.lang['havekey'])
        inp = input(self.lang['havekeyA'])
        if inp in self.confirm:
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
                    del try_key
                    break
                elif ans in self.reject:
                    continue

        # ! Сохранение ключа
        inp = input(self.lang['savekeyA'])
        if inp in self.confirm:
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
        elif inp in self.reject:
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

    def load_key(self, args: list = None):
        """Загрузить ключ"""
        way = ''
        if args is None:
            way = not_exict_check('Введите расположение ключа:')
        else:
            way = args[0]
        self.data[0] = way

    def add(self, args: list = None):
        """Добавляет в базу пароль по введенным меткам"""
        if self.data[0] == '':
            self.load_key()
        if args is None:
            args = input('Введите метки сохранений через пробел:\n')
            args = args.split(' ')
        args[-1] = args[-1] + '.txt'
        args = [self.data[1], *args]
        passw = passinp('Введите пароль:')
        waymaker(args, encrypt(passw, load_key(self.data[0])))

    def remove(self, args: list = None):
        """Удаляет пароль по введенным меткам"""
        if args is None:
            args = input('Введите метки пароля:\n')
            args = args.split(' ')
        args[-1] = args[-1] + '.txt'
        args = [self.data[1], *args]
        args = join(*args)

        if input('Вы уверены? [Y - n]\n') == 'Y':
            remove(args)
        else:
            print('Отмена удаления')

    def list(self):
        """Выводит список всех сохраненых меток"""
        if self.os == 'win':
            from core.mypywindow import wayfinder
            dirs = wayfinder(self.data[1])
            print('Метки сохранений:')
            for i in dirs:
                i = ' '.join(i)
                print(i)

    def view(self, args: list = None):
        """Выводит запрошенный пароль, а так же копирует это в буфер обмена"""
        if args is None:
            args = input('Введите метки пароля:\n')
            args = args.split(' ')
        args[-1] = args[-1] + '.txt'
        args = [self.data[1], *args]
        args = join(*args)

        if self.data[0] == '':
            self.load_key()

        print(write_to_cb(decrypt(load_b_file(args), load_key(self.data[0]))))
