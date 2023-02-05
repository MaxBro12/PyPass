from myengine import UserInp
from core import create_log_file
from handlers import main_check


def main():
    config_dict = main_check()
    process = UserInp(config_dict)
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
