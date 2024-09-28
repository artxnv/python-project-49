from utils import generate_random_number


TASK = "What number is missing in the progression?"


def generate_progression(start, step, length):
    """
    Генерирует арифметическую прогрессию.
    """
    return [start + step * i for i in range(length)]


def hide_element(progression, index):
    """
    Заменяет элемент в прогрессии на '..'.
    """
    hidden_progression = progression[:]
    hidden_progression[index] = '..'
    return hidden_progression


def generate_question():
    """
    Генерирует арифметическую прогрессию с одним скрытым элементом.
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
