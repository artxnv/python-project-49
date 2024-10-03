import random

TASK = 'Ответьте "yes", если данное число простое. Иначе ответьте "no".'


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


def is_prime(number):
    """
    Проверяет, является ли число простым.

    Args:
        number (int): Число для проверки.

    Returns:
        bool: True, если число простое, иначе False.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    """
    Генерирует вопрос о простоте числа и правильный ответ.

    Returns:
        tuple: Вопрос в виде строки и правильный ответ ("yes" или "no").
    """
    number = generate_random_number()
    question = f"Question: {number}"
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer
