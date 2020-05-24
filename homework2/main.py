import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def read_file():
    text = ''
    with open('text.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f]).lower()
    return text


def write_file(encrypted_text):
    with open('./encrypted_text.txt', 'w', encoding='utf8') as f:
        f.write(encrypted_text)


def generate_key():
    alphabet_indexes = list(range(len(alphabet)))
    random.shuffle(alphabet_indexes)
    key = ''.join([alphabet[i] for i in alphabet_indexes])
    with open('./key.txt', 'w', encoding='utf8') as f:
        for i in range(len(alphabet)):
            f.write(f'{alphabet[i]} --- {key[i]}\n')
    return key


def encrypt_text(t):
    text = list(t)
    for i in range(len(text)):
        if text[i] in alphabet:
            index_in_alphabet = alphabet.index(text[i])
            text[i] = key[index_in_alphabet]
    return ''.join(text)


def decrypt_text(t):
    text = list(t)
    for i in range(len(text)):
        if text[i] in alphabet:
            index_in_key = key.index(text[i])
            text[i] = alphabet[index_in_key]
    return ''.join(text)


text = read_file()
key = generate_key()
encrypted_text = encrypt_text(text)
write_file(encrypted_text)
print(text == decrypt_text(encrypted_text))
