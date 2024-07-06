import random
import prompt


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name  # Возвращаем имя пользователя


def play_game(name):  # Принимаем имя пользователя в качестве аргумента
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
    print("Welcome to the Brain Games!")
    name = welcome_user()  # Получаем имя пользователя
    play_game(name)  # Передаем имя пользователя в функцию игры


if __name__ == "__main__":
    main()
