'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit B take-home assignment
'''
import math

#---------- Second Script ------------

#---------- Printing a well formatted invoice ----------
small_beads_price = 9.20
medium_beads_price = 8.52
large_beads_price = 7.98
small_beads = int(input("How many boxes of small beads: "))
total_small = small_beads * small_beads_price
medium_beads = int(input("How many boxes of medium beads: "))
total_medimum = medium_beads * medium_beads_price
large_beads = int(input("How many boxes of large beads: "))
total_large = large_beads * large_beads_price
print("SIZE      QTY    COST PER BOX      TOTALS")
print(f"{'Small':8}{small_beads:>5}{small_beads_price:>16.2f}{total_small:>12.2f}")
print(f"{'Medium':8}{medium_beads:>5}{medium_beads_price:>16.2f}{total_medimum:>12.2f}")
print(f"{'Large':8}{large_beads:>5}{large_beads_price:>16.2f}{total_large:>12.2f}")
print(f"{'Total':29}{total_small + total_medimum + total_large:>12.2f}")

'''
Execution results:
How many boxes of small beads: 10
How many boxes of medium beads: 9
How many boxes of large beads: 8
SIZE      QTY    COST PER BOX      TOTALS
Small      10            9.20       92.00
Medium      9            8.52       76.68
Large       8            7.98       63.84
Total                              232.52

Process finished with exit code 0

How many boxes of small beads: 5
How many boxes of medium beads: 10
How many boxes of large beads: 15
SIZE      QTY    COST PER BOX      TOTALS
Small       5            9.20       46.00
Medium     10            8.52       85.20
Large      15            7.98      119.70
Total                              250.90

Process finished with exit code 0

'''