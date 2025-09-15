import json


def read_txt(filename: str) -> str:
    """
    Читает содержимое текстового файла.
    :param filename: путь к файлу
    :return: строка с содержимым файла
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred while reading the file {filename}: {e}")


def load_json(filename: str) -> dict:
    """
    Загружает данные из json-файла.
    :param filename: путь к файлу
    :return: словарь с содержимым файла
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found")
    except json.JSONDecodeError:
        print(f"File {filename} isn't correct JSON")
    except Exception as e:
        print(f"An error occurred while reading the file {filename}: {e}")


def write_json(data: dict, filename: str) -> None:
    """
    Записывает данные в json-файл.
    :param data: словарь с данными для записи
    :param filename: путь к файлу, в который будут записаны данные
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"An error occurred while saving the file {filename}: {e}")
