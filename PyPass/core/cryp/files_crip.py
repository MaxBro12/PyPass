from .crypo import encrypt, decrypt
from ..filemanage import load_file_bytes, save_file_bytes


def open_cryp_file(way_to_file: str, way_to_key: str):
    return decrypt(load_file_bytes(way_to_file), load_file_bytes(way_to_key))


def open_cryp_file_with_key(way_to_file: str, key: bytes):
    return decrypt(load_file_bytes(way_to_file), key)


def save_cryp_file(way_to_file: str, data: str, way_to_key: str):
    save_file_bytes(way_to_file, encrypt(data, load_file_bytes(way_to_key)))


def save_cryp_file_with_key(way_to_file: str, data: str, key: bytes):
    save_file_bytes(way_to_file, encrypt(data, key))
