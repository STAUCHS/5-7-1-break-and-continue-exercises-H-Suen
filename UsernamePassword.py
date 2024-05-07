#-------------------------------------------------------------------------
# Name:         Username Password
# Purpose:      output if username or pw is correct or incorrect
# Author:       Suen, H.
# Created:      07/05/2024
#-------------------------------------------------------------------------

# input
name = input('Enter your username: ')
pw = input('Enter your password: ')
username = "hansel.suen"
password = "adminadmin"

# processing
while True:
    name = input('Enter your username: ')
    pw = input('Enter your password: ')
    if name != username and pw != password:
        print('Username and password incorrect.')
        continue
    elif name != username and pw == password:
        print('Username incorrect.')
        continue
    elif name == username and pw != password:
        print('Password incorrect.')
        continue
    else:
        print('Welcome!')
        break
    