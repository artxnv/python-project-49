from brain_games.utils import (
    generate_random_number,
    generate_question_with_check
)

TASK = (
    'Answer "yes" if the number is prime. Otherwise answer "no".'
)


def is_prime(number):
    """
    Проверяет, является ли число простым.

    :param number: Число для проверки.
    :return: True, если число простое, иначе False.
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

    :return: Вопрос и правильный ответ.
    """
    number = generate_random_number()
    return generate_question_with_check(number, is_prime)
