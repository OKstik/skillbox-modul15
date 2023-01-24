def get_input_parameters():
    """
    Получаем набор клеток

    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """
    arr_cells = []
    total_cells = int(input('Кол-во клеток: '))
    for i in range(total_cells):
        arr_cells.append(int(input(f'Эффективность {i + 1} клетки: ')))
    return arr_cells

def display_result(cells):
    """
    Выводим список клеток у которых значение меньше индекса

    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """

    print(cells)


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.

    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]

    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """
    arr_cells = []
    i = 1

    for cell in cells:
        if i > cell:
            arr_cells.append(cell)
        i += 1

    return arr_cells


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
