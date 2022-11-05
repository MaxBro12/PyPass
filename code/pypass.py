from userinp import UserInp
from core.debug import create_log_file
from handlers.setup import main_check


def main():
    main_check()
    process = UserInp()
    process.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as er:
        create_log_file(er)
        print(
            'Что-то пошло не так : (\n' +
            'Отправьте файл "error.log" разработчику!\n' +
            'maxbro126@gmail.com'
        )
