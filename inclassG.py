'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit G In-class assignments
'''
import csv

#Hi Professor, since the assignment said "Your script should contain a main function."
#So I will do each part with functions and call those in the main function.
#        Part One  Working with Files

#Create a new file called ZenOfPython.txt and write the first two lines
# of the Zen of Python (see The Zen of Python) to the file. Close the file.
def createFile():
    f = open("ZenOfPython.txt", "w")
    f.write("Beautiful is better than ugly.\n")
    f.write("Explicit is better than implicit.\n")
    f.close()

#Reopen the file and append the 7th and the 17th lines. Then close the file.
def writeFile():
    f = open("ZenOfPython.txt","a+")
    f.write("Readability counts.\n")
    f.write("If the implementation is hard to explain, it's a bad idea.\n")
    f.close()

#Open the file again and read and print the entire contents of the file
# (there shouldn't be any blank lines between the text). Then close the file.
def readFile():
    f = open("ZenOfPython.txt","r")
    for x in f:
        print(x, end='')

#       Part Two  CSV Files

#save  data (but not the header data) into a dictionary. The dictionary key will be a
# tuple consisting of the name of the city and the name of the state.
# The dictionary value will be the population.
def readCSVFile():
    data = {}
    file = open("Cities.csv")
    # Read data from the csv file and save in dictionary data
    readFile = csv.DictReader(file)
    for row in readFile:
        data.update({(row['City'] + " " + row['State']): row['Population']})

    # Print dictionary data
    for x, y in data.items():
        print(x, y)

    # Ask for user input
    print()
    city = input("Please enter a city: ")
    state = input("Please enter a state: ")
    cityState = city + " " + state
    if cityState in data.keys():
        print(f"{cityState} has a population of {data.get(cityState)}")
    else:
        print("No data recorded")

def main():
    createFile()
    writeFile()
    readFile()
    print()
    readCSVFile()

if __name__ == "__main__":
    main()

'''
Execution result:
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064

Please enter a city: Dublin
Please enter a state: California
Dublin California has a population of 46036

Process finished with exit code 0
'''



