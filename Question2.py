#-------------------------------------------------------------------------
# Name:         Question 2
# Purpose:      Add the numbers from 5 to 20, inclusive, but not any multiples of 3
# Author:       Suen, H
# Created:      06-05-2024
#-------------------------------------------------------------------------

x = 4
sum = 0

# processing
while x < 21 :
    x += 1
    if x % 3 == 0:
        continue
    else:
        sum += x
print(sum)