import random

TASK = "Find the greatest common divisor of given numbers."


def generate_random_number(start=1, end=100):
    """
    Генерирует случайное число в заданном диапазоне.

    Args:
        start (int): Начало диапазона (включительно).
        end (int): Конец диапазона (включительно).

    Returns:
        int: Случайное число в заданном диапазоне.
    """
    return random.randint(start, end)


def find_gcd(num1, num2):
    """
    Возвращает наибольший общий делитель (НОД) двух чисел.

    Args:
        num1 (int): Первое число.
        num2 (int): Второе число.

    Returns:
        int: Наибольший общий делитель чисел.
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return abs(num1)


def generate_question():
    """
    Генерирует два числа и правильный ответ (НОД).

    Returns:
        tuple: Вопрос в виде строки и правильный ответ (НОД) в виде строки.
    """
    number1 = generate_random_number(1, 100)
    number2 = generate_random_number(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer
