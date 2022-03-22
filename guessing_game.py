import random
from art import logo

def guessing_game(attempts):
    """
    Checks whether the guessed number is correct
    :param attempts: number of attempts
    :return:
    """
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    if guess == COMP_NUMBER:
        print(f'You got it! The answer was {COMP_NUMBER}.')
        return 0

    attempts = attempts - 1
    if attempts > 0:
        if guess < COMP_NUMBER:
            print('Too low.')
        elif guess > COMP_NUMBER:
            print('Too high.')
        guessing_game(attempts)
    else:
        print(f'You Lose. The answer was {COMP_NUMBER}.')
    return attempts

if __name__ == '__main__':
    COMP_NUMBER = random.randint(1, 100)
    print(logo)
    print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100. ')
    DIFFICULTY = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    if DIFFICULTY == 'easy':
        ATTEMPTS = 10
    elif DIFFICULTY == 'hard':
        ATTEMPTS = 5

    guessing_game(ATTEMPTS)

