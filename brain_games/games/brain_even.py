import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


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


def is_even(number):
    """
    Проверяет, является ли число четным.

    Args:
        number (int): Число для проверки.

    Returns:
        bool: True, если число четное, иначе False.
    """
    return number % 2 == 0


def generate_question():
    """
    Генерирует вопрос о четности числа и правильный ответ.

    Returns:
        tuple: Вопрос в виде строки и правильный ответ ("yes" или "no").
    """
    number = generate_random_number()
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
