import random
import prompt


def is_even(number):
    return number % 2 == 0


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(
        'Answer "yes" if the number is even, '
        'otherwise answer "no".'
    )
    return name


def play_game(name):
    correct_answers_needed = 3
    correct_answers = 0
    while correct_answers < correct_answers_needed:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ").lower()
        correct_answer = 'yes' if is_even(number) else 'no'
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
    name = welcome_user()
    play_game(name)


if __name__ == "__main__":
    main()
