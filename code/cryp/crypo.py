from cryptography.fernet import (
    Fernet,
)
from getpass import getpass


def encrypt(data: str, key: bytes) -> bytes:
    return Fernet(key).encrypt(bytes(data, encoding='UTF-8'))


def decrypt(data: bytes, key: bytes) -> str:
    return Fernet(key).decrypt(data).decode('UTF-8')


def passinp(msg: str):
    return getpass(msg)
