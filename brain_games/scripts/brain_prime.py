import random
import prompt

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def play_game():
    correct_answers_needed = 3
    correct_answers = 0
    
    print('Answer "yes" if given number is prime. Otherwise answer "no."')

    while correct_answers < correct_answers_needed:
        number = random.randint(1, 100)
        print("Question:", number)
        user_answer = prompt.string("Your answer: ").lower()
        correct_answer = 'yes' if is_prime(number) else 'no'
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!")
            return
    print("Congratulations, you won!")

def main():
    print("Welcome to the Brain Games!")  
    play_game() 

if __name__ == "__main__":
    main()
