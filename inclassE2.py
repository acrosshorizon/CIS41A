'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit E In-class assignments
'''

#---------- Second Script -------------

#----------  PART 1 Using range with a for loop.-------------
#Use a for loop to print the even integers in descending order from 10 to 0 inclusive.

for x in range(10,-1,-2):
    print(x)

#----------  PART 2 Looping through dictionary items.-------------
#Create a dictionary named movies and populate it with these key value pairs:
#The Wizard of Oz:1939
#The Godfather:1972
#Lawrence of Arabia:1962
#Raging Bull:1980
movies = {
    "The Wizard of Oz" : 1939,
    "The Godfather" : 1972,
    "Lawrence of Arabia" : 1962,
    "Raging Bull" : 1980
}

#Loop through the dictionary items and print the year in which each movie was made.
# Output should be alpha sorted by movie title.
for key, value in sorted(movies.items()):
    print(f"{key} was made in {value}")

'''
Execution results:
10
8
6
4
2
0
Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939

Process finished with exit code 0

'''
