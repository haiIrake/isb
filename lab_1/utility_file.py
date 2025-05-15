import json


def read_txt(filename: str) -> str:
    """
    Читает содержимое текстового файла.
    :param filename: путь к файлу
    :return: строка с содержимым файла
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_txt(data: str, filename: str) -> None:
    """
    Записывает текст в файл.
    :param data: строка, которая будет записана в файл
    :param filename: путь к файлу, в который будет записан текст
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


def load_key(key_name: str, filename: str) -> int:
    """
    Загружает ключ из json-файла.
    :param key_name: имя ключа
    :param filename: путь к файлу
    :return: ключ
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file).get(key_name)


def load_json(filename: str) -> dict:
    """
    Загружает данные из json-файла.
    :param filename: путь к файлу
    :return: словарь с содержимым файла
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(data: dict, filename: str) -> None:
    """
    Записывает данные в json-файл.
    :param data: данные для записи
    :param filename: путь к файлу
    :return:
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
