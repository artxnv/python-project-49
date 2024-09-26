import random


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
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    question_progression = hide_element(progression, hidden_index)
    question = " ".join(map(str, question_progression))
    correct_answer = str(progression[hidden_index])
    return question, correct_answer
