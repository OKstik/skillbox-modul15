def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: [[165, 163, 160, 160, 157, 157, 155, 154], 162]
    :rtype: List[List[int], int]
    """
    total_container = int(input('Кол-во контейнеров: '))
    arr_container = []

    for _ in range(total_container):
        num = float(input('Введите вес контейнера: '))
        while num > 200 or num % 1 != 0:
            num = float(input('Вы ввели дробное число или число больше 200\nВведите вес контейнера еще раз: '))
        arr_container.append(int(num))

    num = float(input('Введите вес нового контейнера: '))
    while num > 200 or num % 1 != 0:
        num = float(input('Вы ввели дробное число или число больше 200\nВведите вес нового контейнер еще рар: '))
    return [arr_container, num]


def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """

    print('Номер, куда встанет новый контейнер:', serial_number_new_container)


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    index = 0
    for _ in range(len(list_container_weights) - 1):
        if new_container_weight > list_container_weights[index]:
            break
        # тут смотря куда ставить новый ящик, не указанно в описании
        # elif new_container_weight == list_container_weights[index]:
        #    break
        else:
            index += 1
    return index + 1


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
