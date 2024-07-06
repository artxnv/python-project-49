import random
import prompt


def generate_progression(start, step, length):
    """
    Generate an arithmetic progression.

    Args:
        start (int): The starting number of the progression.
        step (int): The difference between consecutive numbers.
        length (int): The length of the progression.

    Returns:
        list: The generated arithmetic progression.
    """
    return [start + step * i for i in range(length)]


def hide_element(progression, index):
    """
    Replace an element in the progression with '..'.

    Args:
        progression (list): The list representing the progression.
        index (int): The index of the element to hide.

    Returns:
        list: The progression with the element at 'index' replaced with '..'.
    """
    hidden_progression = progression[:]
    hidden_progression[index] = '..'
    return hidden_progression


def generate_question():
    """
    Generate a question for the progression game.

    Returns:
        tuple: A tuple containing the full progression, the question with one element hidden,
               and the correct answer (the hidden element).
    """
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    question_progression = hide_element(progression, hidden_index)
    return progression, question_progression, progression[hidden_index]


def welcome_user():
    """
    Welcome the user and request their name.

    Returns:
        str: The user's name.
    """
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    return name


def play_game(name):
    """
    Main logic for the progression game.

    Args:
        name (str): The user's name.
    """
    correct_answers_needed = 3
    correct_answers = 0
    while correct_answers < correct_answers_needed:
        progression, question_progression, hidden_number = generate_question()
        print("Question:", *question_progression)
        user_answer = prompt.integer("Your answer: ")
        if user_answer == hidden_number:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{hidden_number}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    """
    Main function to start the progression game.
    """
    print("Welcome to the Brain Games!")
    name = welcome_user()
    play_game(name)


if __name__ == "__main__":
    main()
