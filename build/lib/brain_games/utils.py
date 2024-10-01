import random


def generate_random_number(start=1, end=100):
    """
    Генерирует случайное число в заданном диапазоне.

    :param start: Начало диапазона.
    :param end: Конец диапазона.
    :return: Случайное число в заданном диапазоне.
    """
    return random.randint(start, end)


def generate_question_with_check(number, check_function):
    """
    Универсальная функция для генерации вопроса и правильного ответа.

    :param number: Число, которое будет проверяться.
    :param check_function: Функция для проверки свойства числа
                           (например, простота или четность).
    :return: Вопрос в виде строки и правильный ответ.
    """
    question = str(number)
    correct_answer = 'yes' if check_function(number) else 'no'
    return question, correct_answer
