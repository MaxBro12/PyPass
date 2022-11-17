from .myos import (
    get_os
)
from .myexcept import (
    KillException as ex,
    OsException,
    ConfigException,
)
from .filemanage import (
    create_folder,
    create_file,
    load_f_list,
    save_f_list,
    load_b_file,
    not_exict_check,
    exict_check,
    waymaker,
)

from .clipb import (
    write_to_cb,
)
