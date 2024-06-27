##########################################################
# Author : Kyle Stranick                                 #
# Class : ITN160                                         #
# Class Section : 401                                    #
# Date : 10/12/2023                                      #
# Assignment:Assignment 7: Number Guessing Game          #
# Version : 3.14                                         #
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
# Version 3.06: created function to ask for min/max numbers to guess between 1-500 called get_bound
# Version 3.06: added loop to ask if you want to choose set min/max values
# Version 3.07: fixed get_roasted to only display after set amount of guesses
# Version 3.08: further expanded get_roasted to not display during correct guess
# Version 3.08: changed update_high_score to display different results based on answers higher. lower,
# and equal to guesses
# Version 3.09: removed unused parameters changed high_score messages
# Version 3.10: moved message to be a constant along with hint and quit_threshold
# Version 3.11: fixed higher_lower function and and get_roasted
# Version 3.12: fixed give hint to only return hint if bool = false
# Version 3.13: fixed parameter but caused by version 3.09 where rand_num value was being reassigned
# Version 3.14: limited distance between min/max values to be at least 20 units apart
#
####################################################################################################

import random
from colorama import Fore, init

init(autoreset=True)

HINT_THRESHOLD = 5
QUIT_THRESHOLD = 15
WELCOME_MESSAGE = f"""{Fore.GREEN}Let's Play A Guessing Game!!'
{Fore.YELLOW}\n'Hi, my name is Hal let's play a game...

    Rules: 

    Don't get too scared it's rather quite simple.
    I'm thinking of a random number.
    Your job as the player is to simply guess the correct number, easy right?!
    If you go the easy route you can just use the 'ol 1 to 100 range just hit enter on selection.
    For those of you that are feeling a little more frisky I'll let you choose any two numbers between 1 and 500.
    FYI, the numbers you pick between WILL ALWAYS have to be at least 20 digits apart. Gotta keep the challenge there!
    Every 5 wrong guesses I will give you a simple hint (don't rely on it too much :-)!!).
    If you cannot guess the number correctly within 15 tries YOU LOSE!! (Which is MORE than generous!)
    I will log your High Score (least number of tries) so try and beat yourself, if you can!'
    """
# Utility Functions


def get_user_input(min_value, max_value):
    """
    Retrieve a valid integer input from the user within a specified range.

    Parameters:
    - min_value (int): The minimum permissible input value.
    - max_value (int): The maximum permissible input value.

    Returns:
    - int: A validated user input as an integer within [min_value, max_value].

    Raises:
    - ValueError: When the provided input is not a valid integer.
    """

    while True:
        try:
            user_input = int(input(Fore.YELLOW + f'\nWhat are ya thinkin\'?: '))
            if min_value <= user_input <= max_value:
                return user_input
            print(Fore.RED + f'\nOnly enter a Number between {min_value} and {max_value}')
        except ValueError:  # handle non int input
            print(Fore.RED + f'\nOnly enter integers please.')


def get_bounds():
    """
    Gets the bounds (minimum and maximum values) for the number to be guessed.

    Prompts the user to input the minimum and maximum values, with default values
    of 1 and 100, respectively. Ensures the provided values are integers, the
    minimum is less than the maximum and that the numbers are 20 units apart.

    Returns:
    - tuple of (int, int): min_value, max_value

     Raises:
    - ValueError: When the provided input is not a valid integer.
    """
    default_min = 1
    default_max = 100

    while True:
        try:
            # Get and validate min_value
            min_value = int(input(Fore.GREEN + f'\nEnter minimum value (default is {default_min}): ') or default_min)
            if 0 <= min_value <= default_max:  # Ensuring min_value is within [0, default_max)
                # If valid, proceed to request max_value
                max_value = int(input(Fore.GREEN + f'Enter max value (default is {default_max}): ') or default_max)
                # Validate max_value
                if min_value + 20 <= max_value <= 500:
                    return min_value, max_value  # If valid, return both values together
                else:
                    print(Fore.RED + f'Max must be  1) larger than min, 2) below 500 and 3) at least '
                                     '20 units away from Min.')
            else:
                print(Fore.RED + f'Min value must be non-negative and less than the default max value.')

        except ValueError:
            print(Fore.RED + f'Input must be an integer.')


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
def get_roasted(try_count, guess_correct):
    """
    Taunts the player at specific attempt counts.

    Parameters:
    - try_count (int): The current number of incorrect guesses made by the player.
    - guess_correct (bool): A flag indicating whether the latest guess was correct.

    Returns:
    - None
    """
    if guess_correct:
        print(Fore.YELLOW + f'\n\'DREAMS DO COME TRUE, IT ONLY TOOK YOU {try_count} '
                            f'{"tries" if try_count > 1 else "try"}\'!')
    else:
        if try_count == 4:
            print(Fore.YELLOW + f'\t\'Do I really need to give you a hint??\'')
        elif try_count == 9:
            print(Fore.YELLOW + f'\t\'Oof don\'t quit your day job\'')
        elif try_count == 14:
            print(Fore.YELLOW + f'\t\'WOW only one more chance to guess correctly... don\'t worry I\'m not holding my '
                                f'breath.\'')


def higher_lower(user_guess, rand_num):
    """
    Checks whether the user’s guess is correct and provides feedback.

    Parameters:
    - user_guess (int): The user's guess.
    - rand_num (int): The target number.

    Returns:
    - bool: True if the user’s guess is correct, False otherwise.
    """

    if user_guess > rand_num:
        print(Fore.GREEN + f'\tHAHA NOPE! GO LOWER!')
        return False
    elif user_guess < rand_num:
        print(Fore.GREEN + f'\tHAHA NOPE! GO HIGHER')
        return False
    else:
        return True


#Response Functions
def give_answer(try_count, rand_num):
    """
    Ends the game if the maximum attempt count is reached.

    Parameters:
    - try_count (int): Current count of tries.
    - rand_num (int): The target number.

    Returns:
    - None
    """

    if try_count == QUIT_THRESHOLD:
        print(Fore.GREEN + f'\n\'Womp Womp :-( the answer was {rand_num}. Luckily I decided to not remove your'
                           f' OS :-P. Better luck next time goodbye!\'')
        exit()


def give_hint(try_count, rand_num, guess_correct):
    """
    Provides a hint if the attempt count reaches a specified threshold.

    Parameters:
    - try_count (int): Current count of tries.
    - rand_num (int): The target number.
    - guess_correct (bool): Whether the last guess was correct.

    Returns:
    - None
    """
    if guess_correct:
        return
    if try_count == HINT_THRESHOLD:
        if rand_num % 2 == 0:
            print(Fore.YELLOW + "\t'I.. I guess you do..... the Answer is EVEN!'")
        else:
            print(Fore.YELLOW + "\t'I.. I guess you do..... the Answer is ODD!'")


# Game State Management
def update_high_score(high_score, try_count):
    """
    Updates and prints the high score based on the latest attempt count.

    Parameters:
    - high_score (int or None): Current high score, or None if not set.
    - try_count (int): The number of tries in the current game.

    Returns:
    - int: Updated high score.

    This function compares the try count with the existing high score and updates
    the high score if the player was able to guess the number in fewer tries.
    Also provides feedback to the player about their performance.
    """
    if high_score is None or 1 < try_count < high_score:
        print(Fore.YELLOW + f'\n\'The new high score is now {try_count} {"tries" if try_count > 1 else "try"}, '
                            f'you got lucky!!\'')
        return try_count
    elif try_count == high_score:
        print(Fore.YELLOW + 'It\'s ok you\'ll beat the high score one day!')  # this is also new
    else:
        print(Fore.YELLOW + f'\nGuess you can\'t beat the record of {high_score} tries. What a shame....')
    return high_score


# Game Loop
def play_round(high_score):
    """
    The function controls the gameplay loop, managing user input, checking guesses,
    providing feedback, hints, and updating the high score accordingly.

    Parameters:
    - high_score (int or None): Current high score, or None if not set.

    Returns:
    - int: Updated high score.
    """
    while True:
        min_value, max_value, = get_bounds()
        rand_num = random.randint(min_value, max_value)

        if should_continue(Fore.YELLOW + f'\nSo you are going to guess between {min_value} and {max_value} (Y/N)?: '):
            print(Fore.YELLOW + f'Good luck guessing, you\'re going to need it.')
            break
    try_count = 0
    while True:
        try_count += 1

        user_guess = get_user_input(min_value, max_value)
        give_answer(try_count, rand_num)
        guess_correct = higher_lower(user_guess, rand_num)
        get_roasted(try_count, guess_correct)
        give_hint(try_count, rand_num, guess_correct)

        if guess_correct:
            high_score = update_high_score(high_score, try_count)
            break
    return high_score


# Game Initialization and Ending:
def welcome_message():
    """
    Prints a welcome message and explains the game rules.
    """
    print(WELCOME_MESSAGE)
    return


def main():
    """
    Execute the primary game loop, managing gameplay and user experience.

    Orchestrates the overall flow of the game, managing game rounds, displaying high
    scores, and handling user interactions and decisions to continue playing.
    """
    welcome_message()
    high_score = None

    while True:  # Display the high score
        if high_score is not None:
            print(Fore.GREEN + f'\nThe current high score is {high_score} {"tries" if high_score > 1 else "try"} '
                               f'can you do better?')

        else:
            print(Fore.GREEN + f'No high score maybe you will be the first!')

        high_score = play_round(high_score)  # Main program loop

        if not should_continue(Fore.GREEN + f'\nWould You Like To Play Again (Y/N)?: '):
            print(Fore.GREEN + f'\nThank You for playing my Number Guessing Game!')
            break


if __name__ == '__main__':
    main()
