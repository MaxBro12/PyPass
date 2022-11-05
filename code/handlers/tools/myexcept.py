class KillException(Exception):
    def __init__(self):
        self.txt = 'Пользователь запустил исключение'
        super().__init__(self.txt)


class OsException(Exception):
    def __init__(self):
        self.txt = 'Неизвестная OS'
        super().__init__(self.txt)
