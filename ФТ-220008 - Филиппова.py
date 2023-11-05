def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha() and char.isascii() and char.isascii():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    while True:
        try:
            text = input("Введите текст, используя английский алфавит: ")
            if not any(char.isalpha() and char.isascii() for char in text):
                raise ValueError
            shift = int(input("Введите шаг сдвига: "))
            break
        except ValueError:
            print("Ошибка ввода! Попробуйте снова.")

    encrypted_text = caesar_encrypt(text, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    print("Зашифрованный текст:", encrypted_text)
    print("Расшифрованный текст:", decrypted_text)


if __name__ == "__main__":
    main()
