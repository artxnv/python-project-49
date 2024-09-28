import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """
    Проверяет, является ли число четным.
    """
    return number % 2 == 0


def generate_question():
    """
    Генерирует вопрос о четности числа и правильный ответ.
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
