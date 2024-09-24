import random
import prompt


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


def welcome_user():
    """
    Приветствует пользователя и объясняет правила игры.
    """
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def play_game(name):
    """
    Основная игровая логика: задаёт вопросы и проверяет ответы пользователя.
    """
    correct_answers_needed = 3
    correct_answers = 0
    while correct_answers < correct_answers_needed:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ").lower()
        correct_answer = 'yes' if is_prime(number) else 'no'
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
