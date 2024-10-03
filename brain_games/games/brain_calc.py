import operator
import random

TASK = "What is the result of the expression?"


def generate_random_number(start=1, end=100):
    """
    Генерирует случайное число в заданном диапазоне.

    Аргументы:
        start (int): Начало диапазона (включительно).
        end (int): Конец диапазона (включительно).

    Возвращает:
        int: Случайное число в заданном диапазоне.
    """
    return random.randint(start, end)


def generate_question():
    """
    Генерирует математическое выражение и правильный ответ.

    Возвращает:
        tuple: Строка с выражением и правильный ответ.
    """
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    num1 = generate_random_number(1, 25)
    num2 = generate_random_number(1, 25)
    op = random.choice(list(operations))
    question = f"{num1} {op} {num2}"
    correct_answer = str(operations[op](num1, num2))
    return question, correct_answer
