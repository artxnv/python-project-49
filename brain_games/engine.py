import prompt


def play(game):
    """
    Основной движок игры, принимает игру в качестве аргумента.
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    correct_answers_needed = 3
    correct_answers = 0

    print(game.TASK)

    while correct_answers < correct_answers_needed:
        question, correct_answer = game.generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
