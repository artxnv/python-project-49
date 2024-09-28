import operator
import random
from brain_games.utils import generate_random_number


TASK = "What is the result of the expression?"


def generate_question():
    """
    Генерирует выражение и правильный ответ.
    """
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    num1 = generate_random_number(1, 25)
    num2 = generate_random_number(1, 25)
    op = random.choice(list(operations.keys()))
    question = f"{num1} {op} {num2}"
    correct_answer = str(operations[op](num1, num2))
    return question, correct_answer
