def get_input_parameters():
    """
    Получаем список видеокарт

    :return: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """

    total_videocards = int(input('Кол-во видеокарт: '))
    arr_videocards = []
    for count in range(total_videocards):
        arr_videocards.append(input(int(f'{count + 1} Видеокарта: ')))
    return arr_videocards


def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт

    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """
    print('старый набор видеокарт, например: ', end='')
    print(old_video_cards)
    print('новый набор видеокарт, например: ', end='')
    print(new_video_cards)


def select_video_cards(video_cards):
    """
    Удаляем из списка видеокарт наибольшие элементы.

    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]

    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """
    max_card = video_cards[0]
    new_arr_videocards = []

    for card in video_cards:
        if card > max_card:
            max_card = card

    for card in video_cards:
        if card == max_card:
            continue
        new_arr_videocards.append(card)

    return new_arr_videocards



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
