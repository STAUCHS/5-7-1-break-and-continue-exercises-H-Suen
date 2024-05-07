#-------------------------------------------------------------------------
# Name:         Question 3
# Purpose:      get the sum of all the numbers from the start to the end
# Author:       Suen, H
# Created:      06-05-2024
#-------------------------------------------------------------------------

# input
start = int(input('Enter the start number: '))
end = int(input('Enter the end number: '))
x = start 

# processing
while x < end:
    x += 1
    if start == 13 or start == 31:
        break
    else:
        start += x
        print(start)