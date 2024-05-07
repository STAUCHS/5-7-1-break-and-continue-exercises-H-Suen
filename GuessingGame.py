#-------------------------------------------------------------------------
# Name:         Guessing Game
# Purpose:      To give the user 5 tries to guess a number from 1 to 100
# Author:       Suen, H.
# Created:      07/05/2024
#-------------------------------------------------------------------------

import random

# welcome
print('*** Guess the Number *** ')
print('Welcome to the guess the number game. ')
print('You have 5 chances to guess the number between 1 and 100.\n')
guess = 0
num = random.randrange(1, 101)

# processing
for i in range(5):
    guess = int(input('Enter a number between 1 and 100: '))
    if i == 4:
        print(f'Sorry, you\'ve guessed incorrectly, the number is {num}.')
        break
    if guess > num:
        print('Too high, guess again\n')
        continue
    elif guess < num:
        print('Too low, guess again\n')
        continue
    else:
        print('Correct!')
        break