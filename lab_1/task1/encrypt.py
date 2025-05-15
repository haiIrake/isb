from lab_1.utility_file import *


def caesar(text: str, alphabet: str, key: int) -> str:
    """
    Шифрует текст с помощью шифра Цезаря.
    :param text: исходный текст
    :param alphabet: алфавит, используемый для шифрования
    :param key: числовой сдвиг для шифра
    :return: строка с зашифрованным текстом
    """
    if not alphabet:
        raise ZeroDivisionError("Alphabet is empty")

    if not str(key).isdigit():
        raise Exception("Key must be a number")

    encrypted = ""

    for char in text:
        match char:
            case c if c in alphabet:
                replace = (alphabet.index(c) + key) % len(alphabet)
                encrypted += alphabet[replace]
            case c if c.lower() in alphabet:
                replace = (alphabet.index(c.lower()) + key) % len(alphabet)
                encrypted += alphabet[replace].upper()
            case _:
               encrypted += char

    return encrypted


def decrypt_caesar(text: str, alphabet: str, key: int) -> str:
    """
    Дешифрует текст, зашифрованный шифром Цезаря.
    :param text: зашифрованный текст
    :param alphabet: алфавит, используемый для шифрования
    :param key: числовой сдвиг для шифра
    :return: строка с дешифрованным текстом
    """
    return caesar(text, alphabet, -key)


def main():
    try:
        task1 = load_json("../settings.json").get("task1")
        text = read_txt(task1.get("TEXT"))

        alphabet = task1.get("ALPHABET")
        key = load_json(task1.get("KEY")).get("KEY")

        encrypted_text = caesar(text, alphabet, key)
        write_txt(encrypted_text, task1.get("ENCRYPTED"))

        print(encrypted_text)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
