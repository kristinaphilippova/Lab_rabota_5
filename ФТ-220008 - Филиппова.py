def encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha() and char.isupper():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_text += encrypted_char
        elif char.isalpha() and char.islower():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha() and char.isupper():
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            decrypted_text += decrypted_char
        elif char.isalpha() and char.islower():
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def validate_alphabet(text):
    for char in text:
        if not char.isalpha() and not char.isnumeric() and not char.isspace():
            return False
    return True

def validate_shift(shift):
    return isinstance(shift, int) and shift > 0

def caesar_cipher():
    text = input('Введите текст: ')
    shift = int(input('Введите шаг сдвига: '))

    if not validate_alphabet(text):
        print('Неверное использование алфавита.')
        return
    if not validate_shift(shift):
        print('Неправильное значение шага сдвига.')
        return

    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print('Зашифрованный текст:', encrypted_text)
    print('Расшифрованный текст:', decrypted_text)

caesar_cipher()
