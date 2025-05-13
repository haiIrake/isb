from lab_1.utility_file import *


def caesar(text: str, alphabet: str, key: int) -> str:
    """
    Шифрует текст с помощью шифра Цезаря.
    :param text: исходный текст
    :param alphabet: алфавит, используемый для шифрования
    :param key: числовой сдвиг для шифра
    :return: строка с зашифрованным текстом
    """
    encrypted = ""
    for char in text:
        if char in alphabet:
            replace = (alphabet.index(char) + key) % len(alphabet)
            encrypted += alphabet[replace]
        elif char.lower() in alphabet:
            replace = (alphabet.index(char.lower()) + key) % len(alphabet)
            encrypted += alphabet[replace].upper()
        else:
            encrypted += char
    return encrypted


def decrypt_caesar(text: str, alphabet: str, key: int) -> str:
    """
    Дешифрует текст, зашифрованный шифром Цезаря.
    """
    return caesar(text, alphabet, -key)


def main():
    try:
        task1 = load_json("../settings.json").get("task1")
        text = read_txt(task1.get("TEXT"))
        alphabet = task1.get("ALPHABET")
        key = load_key("KEY", task1.get("KEY"))

        print("Исходный текст:")
        print(text)

        encrypted_text = caesar(text, alphabet, key)
        write_txt(encrypted_text, task1.get("ENCRYPTED"))

        print("\nЗашифрованный текст:")
        print(encrypted_text)

        print("\nДешифрованный текст:")
        print(decrypt_caesar(encrypted_text, alphabet, key))
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
