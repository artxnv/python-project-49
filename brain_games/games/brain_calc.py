import random
import operator


TASK = "What is the result of the expression?"


def generate_question():
    """
    Генерирует выражение и правильный ответ.
    """
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    op = random.choice(list(operations.keys()))
    question = f"{num1} {op} {num2}"
    correct_answer = str(operations[op](num1, num2))
    return question, correct_answer
