import random
import prompt


def find_gcd(num1, num2):
    """
    Нахождение наибольшего общего делителя (НОД) двух чисел.
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return abs(num1)


def welcome_user():
    """
    Приветствие пользователя и объяснение правил игры.
    """
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    return name


def play_game(name):
    """
    Основная логика игры с запросами и проверкой ответов.
    """
    correct_answers_needed = 3
    correct_answers = 0
    while correct_answers < correct_answers_needed:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f"Question: {number1} {number2}")
        user_answer = prompt.string("Your answer: ")
        correct_answer = str(find_gcd(number1, number2))
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    """
    Основная функция программы.
    """
    print("Welcome to the Brain Games!")
    name = welcome_user()
    play_game(name)


if __name__ == "__main__":
    main()
