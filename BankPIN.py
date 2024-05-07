#-------------------------------------------------------------------------
# Name:         Bank PIN
# Purpose:      make user input pin until correct
# Author:       Suen, H
# Created:      06-05-2024
#-------------------------------------------------------------------------

pin = 0

while pin != 1938:
    pin = int(input('Enter your PIN: '))
    if pin != 1938:
        print('Incorrect PIN. Try again.')
    elif pin == 1938:
        print('PIN accepted. You may now access your account.')