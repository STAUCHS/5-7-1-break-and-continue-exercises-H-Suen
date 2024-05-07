#-------------------------------------------------------------------------
# Name:         Question 4
# Purpose:      Output what they say, if they say stop, output 'GOODBYE!'
# Author:       Suen, H
# Created:      06-05-2024
#-------------------------------------------------------------------------

while True:
    user_input = input('Enter a word: ')
    if user_input == 'stop':
        print('Goodbye!')
        break
    else:
        print(f'Your word: {user_input}\n')
        continue
        