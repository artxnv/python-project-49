import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """
    Проверяет, является ли число простым.
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
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
