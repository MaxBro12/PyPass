def win_hide_file(name: str):
    from win32con import (
        FILE_ATTRIBUTE_HIDDEN,
    )
    from win32api import (
        SetFileAttributes,
    )

    try:
        SetFileAttributes(name, FILE_ATTRIBUTE_HIDDEN)
        return True
    except FileNotFoundError:
        return False
    else:
        return False


def win_show_file(name: str):
    from win32con import (
        FILE_ATTRIBUTE_NORMAL,
    )
    from win32api import (
        SetFileAttributes,
    )

    try:
        SetFileAttributes(name, FILE_ATTRIBUTE_NORMAL)
        return True
    except FileNotFoundError:
        return False
    else:
        return False
