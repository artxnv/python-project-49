from brain_games.utils import generate_random_number

TASK = (
    'Answer "yes" if the number is even, otherwise answer "no."'
)


def is_even(number):
    """
    Проверяет, является ли число четным.

    :param number: Число для проверки.
    :return: True, если число четное, иначе False.
    """
    return number % 2 == 0


def generate_question():
    """
    Генерирует вопрос о четности числа и правильный ответ.

    :return: Вопрос и правильный ответ.
    """
    number = generate_random_number()
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
