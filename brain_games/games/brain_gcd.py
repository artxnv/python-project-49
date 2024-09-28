from brain_games.utils import generate_random_number


TASK = "Find the greatest common divisor of given numbers."


def find_gcd(num1, num2):
    """
    Возвращает наибольший общий делитель двух чисел.
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return abs(num1)


def generate_question():
    """
    Генерирует два числа и правильный ответ (НОД).
    """
    number1 = generate_random_number(1, 100)
    number2 = generate_random_number(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer
