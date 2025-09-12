import math
from scipy.special import gammaincc
from utility_file import *


def frequency_bit_test(sequence: str) -> float:
    """
    Выполняет частотный побитовый тест NIST.
    :param sequence: бинарная последовательность
    :return: P-значение теста
    """
    s_n = abs(sequence.count('1') - sequence.count('0')) / math.sqrt(len(sequence))
    p_value = math.erfc(s_n / math.sqrt(2))

    return p_value


def identical_consecutive_bits_test(sequence: str) -> float:
    """
    Выполняет тест на одинаковые подряд идущие биты.
    :param sequence: бинарная последовательность
    :return: P-значение теста
    """
    n = len(sequence)
    zeta = sequence.count('1') / n

    if abs(zeta - 0.5) >= 2 /math.sqrt(n):
        return 0.0

    v_n = sum(1 if sequence[i] != sequence[i + 1] else 0 for i in range(n - 1))
    p_value = math.erfc(abs(v_n - 2 * n * zeta * (1 - zeta)) / (2 * math.sqrt(2 * n) * zeta * (1 - zeta)))

    return p_value


def longest_sequence_in_block_test(sequence: str, pi: list[float]) -> float:
    """
    Выполняет тест на самую длинную последовательность единиц в блоке.
    :param sequence: бинарная последовательность
    :param pi: список вероятностных констант
    :return: P-значение теста
    """
    blocks = []
    for i in range(0, len(sequence), 8):
        block = sequence[i:i + 8]
        blocks.append(block)

    v = [0, 0, 0, 0]

    for block in blocks:
        max_len = 0
        cur_len = 0

        for bit in block:
            if bit == '1':
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0

        match max_len:
            case x if x <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1

    chi2 = sum(((v[i] - 16 * pi[i]) ** 2) / (16 * pi[i]) for i in range(4))
    p_value = gammaincc(3 / 2, chi2/ 2)

    return p_value


def analyze_sequence(sequence: str, pi: list[float]) -> dict:
    """
    Выполняет тесты NIST для данной последовательности.
    :param sequence: бинарная последовательность
    :param pi: список вероятностных констант
    :return: словарь с результатами тестов
    """
    return {
        "sequence": sequence,
        "frequency_bit_test": frequency_bit_test(sequence),
        "identical_consecutive_bits_test": identical_consecutive_bits_test(sequence),
        "longest_sequence_in_block_test": longest_sequence_in_block_test(sequence, pi)
    }


def main():
    source = load_json("settings.json")
    cpp_seq = read_txt(source["CPP"])
    java_seq = read_txt(source["JAVA"])

    results = {
        "cpp": analyze_sequence(cpp_seq, source["PI"]),
        "java": analyze_sequence(java_seq, source["PI"])
    }

    write_json(results, source["RESULTS"])
    print(f"Результаты сохранены в {source["RESULTS"]}")


if __name__ == "__main__":
    main()
