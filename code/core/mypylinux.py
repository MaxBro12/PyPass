from os import (
    rename,
)


def lin_hide_file(name: str):
    try:
        rename(name, '.' + name)
        return True
    except FileNotFoundError:
        return False
    else:
        return False
