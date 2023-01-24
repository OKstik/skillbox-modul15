def get_input_parameters():
    """
    Получаем список фильмов, которые пользователь хочет добавить в "любимые"

    :return: добавляемые фильмы, например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :rtype: List[str]
    """
    movies = int(input('Сколько фильмов хотите добавить? '))
    arr_movies = []

    for _ in range(movies):
        arr_movies.append(input('Введите название фильма: '))
    return arr_movies


def display_result(favorite_films, errors):
    """
    Выводим список ошибок и список любимых фильмов

    :param favorite_films: список любимых фильмов, например: ["Леон", "Мементо"]
    :type favorite_films: List[str]
    :param errors: список ненайденных фильмов, например: ["Безумный Макс", "Царь горы"]
    :type errors: List[str]
    """
    print()
    for movie in errors:
        print(f'Ошибка: фильма {movie} у нас нет :(')

    print(f'Ваш список любимых фильмов: ', end='')
    for i in range(len(favorite_films) - 1):
        print(favorite_films[i], end=', ')
    print(favorite_films[-1], end='')


def add_favorite_film(new_favorite_films, available_films):
    """
    Добавляем фильмы в список "любимых".
    :param new_favorite_films: фильмы, которые нужно добавить в "любимые",
           например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :type new_favorite_films: List[str]
    :param available_films: фильмы, которые есть на киносайте,
           например: ["Леон", "Назад в будущее", "Мементо"]
    :type available_films: List[str]

    :return: Список фильмов в списке "любимых" и список не найденных фильмов,
             например: (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
    :rtype: Tuple[List[str], List[str]]
    """

    add_movie = []
    unfinished_movies = []

    for new_movie in new_favorite_films:
        for av_film in available_films:
            if new_movie == av_film:
                add_movie.append(new_movie)
                break
        else:
            unfinished_movies.append(new_movie)
    return add_movie, unfinished_movies


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
