from datacsv import Table


progRun = True


def stop():
    global progRun
    progRun = False


def help_fun():
    print('Вот список всех команд:\n'
          '\t"stop" - остановит программу\n'
          '\t"view" - откроет предпросмотр\n'
          '\t"viewc" - откроет информацию об определенной метке\n'
          '\t"add" - добавить строку в конец таблицы\n'
          '\t"remove" - удалить строку из таблицы\n'
          )


a = Table()
commands = {
    "stop": stop,
    "help": help_fun,
    "add": a.add,
    "remove": a.remove,
    "load": a.read_txt,
    "save": a.save_txt,
    "view": a.view,
    "viewc": a.view_current
    }


def user_input():
    word = str(input(': ')).split()
    com = word[0]
    if com in commands:
        command = commands[com]
        try:
            if len(word) > 1:
                addition = word[1::]
                return command(addition)
            else:
                return command()
        except TypeError:
            print('Неверная команда!')
            user_input()
    else:
        print(f'Неизвестная команда: "{com}"')


if __name__ == '__main__':
    print('Приветствую в закрытой версии шифратора паролей!\nИспользуйте команду "help"')
    while progRun:
        user_input()