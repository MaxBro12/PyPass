from cryptography.fernet import Fernet


def create_key() -> bytes:
    return Fernet.generate_key()


def save_key(key, name: str):
    with open(name, 'wb') as f:
        f.write(key)


def load_key(name: str) -> bytes:
    return open(name, 'rb').read()
