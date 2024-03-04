from core import wayfinder, open_cryp_file, open_cryp_file_with_key, save_cryp_file, save_cryp_file_with_key, read_toml_string, toml_type_check, write_to_toml_str
from settings import FILE_SETTINGS, FILE_SETTINGS_KEY, SETTINGS_IN, FILE_SETTINGS_KEY


def main_check():
    if not wayfinder(FILE_SETTINGS):
        create_settings()
    else:
        if not toml_type_check(SETTINGS_IN, read_toml_string(open_cryp_file_with_key(FILE_SETTINGS, FILE_SETTINGS_KEY))):
            create_settings()

def create_settings():
    save_cryp_file_with_key(FILE_SETTINGS, write_to_toml_str(SETTINGS_IN), FILE_SETTINGS_KEY)
