import random
from colorama import Fore, init

init(autoreset=True)
# Version 1.01: created base program with basic syntax
# Version 1.02: added high score function
# Version 1.02: added if conditional statements to state try/tries


def should_continue(prompt):
    while True:
        response = input(prompt).upper()
        if response in ['Y', 'N']:
            return response == 'Y'
        print('\nInvalid input. Please enter Y or N.\n')


def main():
    print('Welcome to the Number Guessing Game!')
    high_score = None  # to always start with no value

    while True:  # Display the high score
        if high_score is not None:
            print(f'The current high score is {high_score} {"tries" if high_score > 1 else "try"}.')

        else:
            print('No high score maybe you will be the first!')
        number_to_guess = random.randint(1, 100)
        guess_count = 0

        while True:
            guess_count += 1
            try:
                user_guess = int(input('What is your guess?: '))

                if user_guess > number_to_guess:
                    print(f'Your guess is too high try again!')
                elif user_guess < number_to_guess:
                    print('Your Guess is too low try again!')
                else:
                    print(Fore.GREEN + f'CONGRATULATION YOU GUESSED CORRECTLY IN {guess_count} TRIES!!')
                    if high_score is None or guess_count < high_score:
                        high_score = guess_count  # saves high score for each round
                        print("New high score!")
                    break
            except ValueError:
                print('Only enter a number between 1 and 100!')

        if not should_continue('Would You Like To Play Again (Y/N)? '):
            print('\nThank You for playing the Number Guessing Game!')


if __name__ == '__main__':
    main()
