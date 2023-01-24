def get_input_parameters():
    """
    Получаем входное слово

    :return: входное слово, например: "привет"
    :rtype: str
    """
    return input('Введите слово: ')


def display_result(number_unique_letters):
    """
    Выводим количество уникальных букв в слове

    :param number_unique_letters: количество уникальных букв в слове, например: 6
    :type number_unique_letters: int
    """
    print('Кол-во уникальных букв:', number_unique_letters)


def count_number_unique_letters(word):
    """
    Считаем количество уникальных букв в слове.

    :param word: входное слово, например: "привет"
    :type word: str

    :return: количество уникальных букв в слове, например: 6
    :rtype: int
    """
    total_rep = 0
    for ch in word:
        rep = 0
        for rep_ch in word:
            if ch == rep_ch:
                rep += 1
        if rep < 2:
            total_rep += 1

    return total_rep


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
