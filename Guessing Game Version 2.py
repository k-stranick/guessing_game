import random
from colorama import Fore, init

init(autoreset=True)

# Version 2.01: took program and defined individual functions for maintainability
# Version 2.02: fixed def updated_high_score always returning none error
# Version 2.02: made check_guess return bool values


def should_continue(prompt):
    """
    Query the user to decide whether to continue with the program.

    Parameters:
    - prompt (str): A string to display when requesting input from the user.

    Returns:
    - bool: True if the user enters 'Y', False if the user enters 'N'.

    The function continuously prompts the user until a valid input (Y/N) is provided,
    ensuring that the program only proceeds with a clear affirmative or negative from the user.
    """
    while True:
        response = input(prompt).upper()
        if response in ['Y', 'N']:
            return response == 'Y'
        print('\nInvalid input. Please enter Y or N.\n')


def update_high_score(high_score, try_count):
    if high_score is None or try_count < high_score:
        print("New high score!")
        return try_count
    return high_score  # updated to fix poor return value always 0


def get_user_input():
    while True:
        try:  # def function
            user_input = int(input('What is your guess?: '))
            if 1 <= user_input <= 100:
                return user_input
            print('Number out of range. Please guess a number between 1 and 100')
        except ValueError:  # handle non int input
            print('Only enter a Number between 1 and 100')


def check_guess(user_guess, number_to_guess):
    # def function
    if user_guess > number_to_guess:
        print(f'Your guess is too high try again!')
        return False
    elif user_guess < number_to_guess:
        print('Your guess is too low try again!')
        return False
    else:
        print(Fore.GREEN + f'CONGRATULATION YOU GUESSED CORRECTLY!')
        return True


def play_round(high_score):
    # def function
    number_to_guess = random.randint(1, 100)
    try_count = 0

    while True:  # main program loop
        try_count += 1
        user_guess = get_user_input()

        if check_guess(user_guess, number_to_guess):
            print(f'It took you {try_count} {"tries" if try_count > 1 else "try"} to guess correctly!')
            high_score = update_high_score(high_score, try_count)
            break
    return high_score


def main():
    print('Welcome to the Number Guessing Game!')
    high_score = None

    while True:  # Display the high score
        if high_score is not None:
            print(f'The current high score is {high_score} {"tries" if high_score > 1 else "try"}.')

        else:
            print('No high score maybe you will be the first!')

        high_score = play_round(high_score)

        if not should_continue('Would You Like To Play Again (Y/N)? '):
            print('\nThank You for playing the Number Guessing Game!')
            break


if __name__ == '__main__':
    main()
