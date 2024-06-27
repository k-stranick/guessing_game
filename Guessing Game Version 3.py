##########################################################
# Author : Kyle Stranick                                 #
# Class : ITN160                                         #
# Class Section : 401                                    #
# Date : 10/11/2023                                      #
# Assignment:Assignment 7: Number Guessing Game          #
# Version : 3.05                                         #
##########################################################

###################
#Syntax References:
###################
# code academy go APP
# Cannon, Jason. (2016). Python Succinctly., Syncfusion Inc.
# Gupta, Anubhav. Slither into Python. (2021?)
# Murach, Mike. (2021). Murach's Python Programming (2nd Ed.), Mike Murach & Associates, Inc.
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# https://www.tutorialspoint.com/python/python_if_else.htm
# https://www.tutorialspoint.com/python/python_functions.htm
# https://www.w3schools.com/python/
# https://www.pluralsight.com  I have a subscription
# https://www.w3schools.com/python/python_dictionaries.asp
# https://initialcommit.com/blog/python-isalpha-string-method
# https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
# https://www.geeksforgeeks.org/python-test-if-string-contains-alphabets-and-spaces/
# https://www.geeksforgeeks.org/find-average-list-python/
# https://code-basics.com/languages/python/lessons/magic-numbers
# https://wiki.python.org/moin/HandlingExceptions
# https://wiki.python.org/moin/ForLoop
# https://wiki.python.org/moin/WhileLoop
# https://docs.python.org/3/tutorial/datastructures.html
# https://guicommits.com/organize-python-code-like-a-pro/
# https://docs.python-guide.org/writing/structure/
# https://www.askpython.com/python/examples/generate-random-colors#:~:text=Using%20the%20random%20module&text=We%20can%20implement%20it%20to%20generate%20random%20colors.&text=Here%20we%20have%20created%20a,returns%20them%20as%20a%20tuple.
# https://stackoverflow.com/questions/16726354/saving-the-highscore-for-a-game <- implement??
# https://stackoverflow.com/questions/63769198/giving-one-hint-for-each-of-the-tries-guessing-number-game
#
################
# Version Notes:
################
# Version 1.01: created base program with basic syntax
# Version 1.02: added high score function
# Version 1.02: added if conditional statements to state try/tries
#
# Version 2.01: took program and defined individual functions for maintainability
# Version 2.02: fixed def updated_high_score always returning none error
# Version 2.02: made check_guess return bool values
#
# Version 3.01: organized and labeled code structure for readability
# Version 3.01: added docstring to explain code better
# Version 3.02: added get_roasted def to taunt players
# Version 3.02: changed overall program to feel more like a game with written language and taunts.
# Version 3.03: changed color scheme of game
# Version 3.04: removed empty return values for give_hint and give_answer
# Version 3.04: set give_hint to only return even or odd not higher or lower
# Version 3.05: set give_hint and get_roasted for == for set counts instead of constantly repeating
####################################################################################################

import random
from colorama import Fore, init

init(autoreset=True)


# Utility Functions
def get_user_input():
    """
    Fetches and validates user input to ensure it is an integer within [1, 100].

    Returns:
    - int: A number provided by the user.
    """
    while True:
        try:
            user_input = int(input(Fore.YELLOW + f'\nWhat are ya thinkin\'?: '))
            if 1 <= user_input <= 100:
                return user_input
            print(Fore.RED + f'\nNumber out of range. Please guess a number between 1 and 100')
        except ValueError:  # handle non int input
            print(Fore.RED + f'\nOnly enter a Number between 1 and 100')


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
        print(Fore.RED + f'\nInvalid input. Please enter Y or N.\n')


# Game Logic Functions
def get_roasted(try_count):  # had to fix logical order then switch from > to equal to stop constant display
    """
    Taunts the player at specific attempt counts.

    Parameters:
    - try_count (int): Current count of tries.

    Returns:
    - None
    """
    if try_count == 4:
        print(Fore.YELLOW + '\t\'Do I really need to give you a hint??\'')
    elif try_count == 9:
        print(Fore.YELLOW + f'\t\'oof don\'t quit your day job\'')
    elif try_count == 14:
        print(Fore.YELLOW + f'\t\'WOW only one more chance to guess correctly... don\'t worry I\'m not holding my '
                            f'breath.\'')


def check_guess(user_guess, number_to_guess, try_count):
    """
    Checks whether the user’s guess is correct and provides feedback.

    Parameters:
    - user_guess (int): The user's guess.
    - number_to_guess (int): The target number.
    - try_count (int): The current attempt count.

    Returns:
    - bool: True if the user’s guess is correct, False otherwise.
    """
    if user_guess > number_to_guess:
        print(Fore.GREEN + f'\tHAHA NOPE! GO LOWER!')
        return False
    elif user_guess < number_to_guess:
        print(Fore.GREEN + f'\tHAHA NOPE! GO HIGHER')
        return False
    else:
        print(Fore.YELLOW + f'\n\'DREAMS DO COME TRUE, IT ONLY TOOK YOU {try_count} '
                            f'{"tries" if try_count > 1 else "try"}\'!')
        return True


#Response Functions
def give_answer(try_count, quit_threshold, number_to_guess):
    """
    Ends the game if the maximum attempt count is reached.

    Parameters:
    - try_count (int): Current count of tries.
    - quit_threshold (int): Maximum allowed attempts.
    - number_to_guess (int): The target number.

    Returns:
    - None
    """
    if try_count == quit_threshold:
        print(Fore.GREEN + f'\n\'Womp Womp :-( the answer was {number_to_guess}. Luckily I decided to not remove your'
                           f' OS :-P. Better luck next time.\'')
        exit()


def give_hint(try_count, hint_threshold, number_to_guess):
    """
    Provides a hint if the attempt count reaches a specified threshold.

    Parameters:
    - try_count (int): Current count of tries.
    - hint_threshold (int): Attempt count at which a hint is provided.
    - number_to_guess (int): The target number.

    Returns:
    - None
    """
    if try_count == hint_threshold:
        if number_to_guess % 2 == 0:
            print(Fore.YELLOW + '\t\'I.. I guess you do..... the Answer is EVEN!\'')
        else:
            print(Fore.YELLOW + '\t\'I.. I guess you do..... the Answer is ODD!\'')


# Game State Management
def update_high_score(high_score, try_count):
    """
    Updates and prints the high score based on the latest attempt count.

    Parameters:
    - high_score (int or None): Current high score, or None if not set.
    - try_count (int): The number of tries in the current game.

    Returns:
    - int: Updated high score.
    """
    if high_score is None or try_count < high_score:
        print(Fore.YELLOW + f'\n\'The new high score is now {try_count} {"tries" if try_count > 1 else "try"}, '
                            f'you got lucky!!\'')
        return try_count
    else:
        print(Fore.YELLOW + f'\nGuess you can\'t beat the record of {high_score} tries. What a shame....')
        return high_score


# Game Loop
def play_round(high_score, hint_threshold=5, quit_threshold=15):
    """
    Executes a round of the game, where the user tries to guess the target number.

    Parameters:
    - high_score (int or None): Current high score, or None if not set.
    - hint_threshold (int): The number of wrong guesses allowed before giving a hint. Default: 5.
    - quit_threshold (int): The number of wrong guesses allowed before ending the game. Default: 15.

    Returns:
    - int: Updated high score.
    """
    number_to_guess = random.randint(1, 100)
    try_count = 0

    while True:
        try_count += 1

        user_guess = get_user_input()
        give_hint(try_count, hint_threshold, number_to_guess)
        give_answer(try_count, quit_threshold, number_to_guess)
        get_roasted(try_count)

        if check_guess(user_guess, number_to_guess, try_count):
            high_score = update_high_score(high_score, try_count)
            break
    return high_score


# Game Initialization and Ending:
def welcome_message():
    """
    Prints a welcome message and explains the game rules.
    """
    print(Fore.GREEN + '\nLet\'s Play A Guessing Game!!')
    print(Fore.YELLOW + '''\n'Hi, my name is Hal let's play a game...

    Rules: 

    Don't get too scared it's rather quite simple.
    I'm thinking of a number between 1 and 100.
    Your job as the player is to simply guess the correct number, easy right?!
    Every 5 wrong guesses I will give you a simple hint.
    If you cannot guess the number correctly within 15 tries YOU LOSE!!
    I will log your High Score (least number of tries) so try and beat yourself, if you can!'
    ''')


def main():
    """
    Orchestrates the game flow, managing rounds and user interactions.
    """
    welcome_message()
    high_score = None

    while True:  # Display the high score
        if high_score is not None:
            print(Fore.GREEN + f'\nThe current high score is {high_score} {"tries" if high_score > 1 else "try"} '
                               f'can you do better?')

        else:
            print(Fore.GREEN + 'No high score maybe you will be the first!')

        high_score = play_round(high_score)

        if not should_continue(Fore.GREEN + '\nWould You Like To Play Again (Y/N)?: '):
            print(Fore.GREEN + '\nThank You for playing my Number Guessing Game!')
            break


if __name__ == '__main__':
    main()
