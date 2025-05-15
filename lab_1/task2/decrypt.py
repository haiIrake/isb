from lab_1.utility_file import *


def get_frequency(text: str) -> dict:
    """
    Вычисляет частоту каждого символа в тексте.
    :param text: входной текст
    :return: словарь, в котором ключи - символы, а значения - их частоты
    """
    freq_dict = {}

    for char in text:
        if char.lower() in freq_dict:
            freq_dict[char.lower()] += 1
        else:
            freq_dict[char.lower()] = 1

    for char, count in freq_dict.items():
        freq_dict[char] = count / len(text)

    return dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))


def get_key(freq_dict1: dict, freq_dict2: dict) -> dict:
    """
    Создаёт ключ путём сопоставления ключей из двух входных словарей.
    :param freq_dict1: словарь частот зашифрованного текста
    :param freq_dict2: словарь частот языка
    :return: словарь замен, в котором символы зашифрованного текста сопоставляются с
    наиболее вероятными оригинальными символами
    """
    return {k1: k2 for k1, k2 in zip(freq_dict1.keys(), freq_dict2.keys())}


def decrypt(text: str, key: dict) -> str:
    """
    Заменяет символы в тексте согласно переданному ключу.
    :param text: исходный текст
    :param key: словарь замен
    :return: новый текст, в котором символы заменены в соответствии с ключом
    """
    decrypted = ""

    for char in text:
        decrypted_char = key.get(char.lower())
        if decrypted_char is None:
            decrypted_char = char.lower()
        decrypted += decrypted_char

    return decrypted


def main():
    try:
        task2 = load_json("../settings.json").get("task2")
        encrypted = read_txt(task2.get("ENCRYPTED"))

        frequency = get_frequency(encrypted)
        write_json(frequency, task2.get("FREQUENCY"))

        rus_frequency = load_json(task2.get("RUS_FREQUENCY"))

        key = get_key(frequency, rus_frequency)
        write_json(key, task2.get("KEY"))

        decrypted_text = decrypt(encrypted, key)
        write_txt(decrypted_text, task2.get("DECRYPTED"))

        right_key = load_json(task2.get("RIGHT_KEY"))

        decrypted = decrypt(encrypted, right_key)
        write_txt(decrypted, task2.get("READ_DECRYPTED"))

        print(decrypted)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
