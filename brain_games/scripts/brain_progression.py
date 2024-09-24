import random
import prompt


def generate_progression(start, step, length):
    """
    Генерирует арифметическую прогрессию заданной длины.

    :param start: Начальное число прогрессии.
    :param step: Шаг прогрессии.
    :param length: Длина прогрессии.
    :return: Список чисел, составляющих прогрессию.
    """
    return [start + step * i for i in range(length)]


def hide_element(progression, index):
    """
    Заменяет элемент прогрессии на '..' для игры.

    :param progression: Список чисел прогрессии.
    :param index: Индекс элемента, который нужно скрыть.
    :return: Прогрессия с заменённым элементом.
    """
    hidden_progression = progression[:]
    hidden_progression[index] = '..'
    return hidden_progression


def generate_question():
    """
    Генерирует вопрос и правильный ответ для игры.

    :return: Прогрессия, прогрессия с скрытым элементом и скрытое число.
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
    Приветствует пользователя и объясняет правила игры.

    :return: Имя пользователя.
    """
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    return name


def play_game(name):
    """
    Основная игровая логика.

    :param name: Имя пользователя.
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
    Основная функция программы.
    """
    print("Welcome to the Brain Games!")
    name = welcome_user()
    play_game(name)


if __name__ == "__main__":
    main()
