'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit E take-home assignment
'''
import random

#---------- Third Script ------------
#---------- Part One – Looping with String Methods ------------

#Assign the text "Believe you can and you're halfway there." to a variable called quote
quote = "Believe you can and you're halfway there."
#Loop through the quote to find and print the index of all the "a" characters.
count = 0
for x in range(len(quote)):
    if x == quote.find("a",x, len(quote)):
        print(f"a found at index {x}")
        x = quote.find("a") + 1
    else:
        x += 1
#---------- Part Two – Nested Loops ------------
#Ask user input
row = int(input("\nPlease enter the number of rows for the multiplication table: "))
y = 1

#Nested loop to print
for x in range(row):
    for y in range(row):
        if y <= x:
            print(f"{(x+1) * (y + 1): 4}", end = '')
    print()

'''
Execution results:
a found at index 13
a found at index 16
a found at index 28
a found at index 32

Please enter the number of rows for the multiplication table: 12
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   6  12  18  24  30  36
   7  14  21  28  35  42  49
   8  16  24  32  40  48  56  64
   9  18  27  36  45  54  63  72  81
  10  20  30  40  50  60  70  80  90 100
  11  22  33  44  55  66  77  88  99 110 121
  12  24  36  48  60  72  84  96 108 120 132 144
'''
