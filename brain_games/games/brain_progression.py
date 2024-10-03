import random

TASK = "What number is missing in the progression?"


def generate_random_number(start=1, end=100):
    """
    Генерирует случайное число в заданном диапазоне.

    Args:
        start (int): Начало диапазона (включительно).
        end (int): Конец диапазона (включительно).

    Returns:
        int: Случайное число в заданном диапазоне.
    """
    return random.randint(start, end)


def generate_progression(start, step, length):
    """
    Генерирует арифметическую прогрессию.

    Args:
        start (int): Начальное число прогрессии.
        step (int): Шаг прогрессии.
        length (int): Длина прогрессии.

    Returns:
        list: Арифметическая прогрессия.
    """
    return [start + step * i for i in range(length)]


def hide_element(progression, index):
    """
    Заменяет элемент в прогрессии на '..'.

    Args:
        progression (list): Арифметическая прогрессия.
        index (int): Индекс элемента, который нужно скрыть.

    Returns:
        list: Прогрессия с заменённым элементом.
    """
    hidden_progression = progression[:]
    hidden_progression[index] = '..'
    return hidden_progression


def generate_question():
    """
    Генерирует арифметическую прогрессию с одним скрытым элементом.

    Returns:
        tuple: Вопрос в виде строки и правильный ответ.
    """
    start = generate_random_number(1, 10)
    step = generate_random_number(1, 10)
    length = generate_random_number(5, 10)
    progression = generate_progression(start, step, length)
    hidden_index = generate_random_number(0, length - 1)
    question_progression = hide_element(progression, hidden_index)
    question = " ".join(map(str, question_progression))
    correct_answer = str(progression[hidden_index])
    return question, correct_answer
