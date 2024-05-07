#-------------------------------------------------------------------------
# Name:         Question 1
# Purpose:      To count to 10, skipping 7
# Author:       Suen, H
# Created:      06-05-2024
#-------------------------------------------------------------------------

# processing
num = -1
while True:
    num += 1
    if num == 7:
        continue
    if num > 10:
        break
    print(num)