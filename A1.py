import csv

data = {}
file = open("Cities.csv")
#Read data from the csv file and save in dictionary data
readFile = csv.DictReader(file)
for row in readFile:
        data.update({(row['City'] + " " + row['State']): row['Population']})

#Print dictionary data
for x, y in data.items():
        print(x,y)

#Ask for user input
print()
city = input("Please enter a city: ")
state = input("Please enter a state: ")
cityState = city + " " + state
if cityState in data.keys():
        print(f"{cityState} has a population of {data.get(cityState)}")
else:
        print("No data recorded")

