all_simb = ' ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890!@#$%^&*()_-+\\|/.,;:\'"`~abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя\n\t'
all_simb = tuple(all_simb)


def list_rewind(list_of_val: list, rewind_val: int):
    return list_of_val[rewind_val:] + list_of_val[:rewind_val]


def encrypt(text: str, key: int):
    return bits_convert(text_to_bits(caesar_enc(text, key)))


def decrypt(text_in_bits: str, key: int):
    return caesar_dec(text_from_bits(bits_convert(text_in_bits)), key)


def encrypt_lite(text: str, key: int):
    return caesar_enc(text, key)


def decrypt_lite(text_in_bits: str, key: int):
    return caesar_dec(text_in_bits, key)


def caesar_enc(text: str, key: int = 0):
    new_text = ''
    enc_simb = list_rewind(all_simb, key)
    for i in text:
        mesto = all_simb.index(i)
        new_text += enc_simb[mesto]
    return str(new_text)


def caesar_dec(text: str, key: int = 0):
    new_text = ''
    enc_simb = list_rewind(all_simb, -key)
    for i in text:
        mesto = all_simb.index(i)
        new_text += enc_simb[mesto]
    return str(new_text)


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def bits_convert(bits):
    new_bits = ''
    for i in bits:
        match i:
            case '0':
                new_bits += '1'
            case '1':
                new_bits += '0'
    return new_bits


#file = open('data.txt', 'r')
#text = file.readlines()[0]
#print(decrypt(text, 10))