'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit A take-home assignment
'''

import math
#######################################################
# ------  Function from the math module ------
#######################################################
#a. Ask the user for a number (test with the value 7.6).
number = float (input("Plese enter a number: "))

#b Print the square root of the number, rounded to two decimal places (include an appropriate description).
print(round(math.sqrt(number), 2))

#c. Print the base-10 log of the number, rounded to two decimal places (include an appropriate description)
print(round(math.log(number, 10),2))

'''
Execution results:
Plese enter a number: 7.6
2.76
0.88
'''