#-------------------------------------------------------------------------
# Name:         Dice Doubles
# Purpose:      to roll 2 dice and stop if the rolls are the same
# Author:       Suen, H.
# Created:      07/05/2024
#-------------------------------------------------------------------------

import random

# welcome
print('HERE COMES THE DICE!\n')

# processing
while True:
    roll_1 = random.randrange(1, 7)
    roll_2 = random.randrange(1, 7)
    sum = roll_2 + roll_1
    print(f'Roll #1: {roll_1}')
    print(f'Roll #2: {roll_2}')
    print(f'The total is {sum}!\n')
    if roll_1 == roll_2:
        break