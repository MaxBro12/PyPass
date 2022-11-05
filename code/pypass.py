from userinp import UserInp
from handlers.debug import create_log_file


def main():
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
