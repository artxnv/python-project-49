import random
import operator
import prompt

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def generate_question():
    """Generate a question and its correct answer."""
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    op = random.choice(list(OPERATORS.keys()))
    question = (
        f"What is the result of the expression? "
        f"{num1} {op} {num2}"
    )
    correct_answer = str(OPERATORS[op](num1, num2))
    return question, correct_answer


def welcome_user():
    """Welcome the user and ask for their name."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")


def play_game():
    """Main game logic."""
    correct_answers_needed = 3
    correct_answers = 0
    while correct_answers < correct_answers_needed:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!")
            return
    print("Congratulations!")


def main():
    """Main function of the game."""
    print("Welcome to the Brain Games!")
    welcome_user()
    play_game()


if __name__ == "__main__":
    main()
