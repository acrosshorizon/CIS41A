'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit G take-home assignment
'''
#                                   Part One – Reading a data file
f = open("States.txt", "r")
#I created a parallel list of list to store data read from file
dataList = [list(), list(), list()]
for row in f:
    index = 0
    for x in row.split():
        dataList[index].append(x)
        index += 1

#I created a loop to find the highest value of the population (dataList[2])
#of the Midwest (in dataList[1])
highest = 0
track = 0
for x in dataList[1]:
    if x == "Midwest" and int(dataList[2][track]) > int(highest):
        highest = dataList[2][track]
        highestPopStates = dataList[0][track]
    track += 1
print(f"Highest population state in the Midwest is: {highestPopStates} {highest}\n")

#                                   Part Two – A Dictionary of Lists
f = open("USPresidents.txt", "r")
states = list()
president = list()
table = [states, president]
#Read file and store in lists
for row in f:
    index = 0
    for x in row.split():
        table[index].append(x)
        index +=1

#Create an empty dictionary and story all the key with empty values
presidentDict = {}
for x in states:
    presidentDict[x] = ""
#Assign value to each key
for x in presidentDict.keys():
    sameStates = list()
    for y in president:
        if states[president.index(y)] == x:
            sameStates.append(y)
    presidentDict[x] = sameStates

#Find the states has most president from key list and value list of dictionary
count = 0
key = list(presidentDict.keys())
value = list(presidentDict.values())
for x in value:
    if len(x) > count:
        count = len(x)
        bestStates = key[value.index(x)]
#Print result
print(f"The state with the most presidents is {bestStates} with {count} presidents:")
for x in presidentDict[bestStates]:
    print(x)

#                           Part Three – Dictionary Keys and Sets

#second dictionary from the USPresidents.txt file described in the previous exercise. Each key will again be a state abbreviation,
# however, the value will be the count of presidents from that state.
#I will use the previous parallel key and value lists that I created in part 2 to store in my second dict
secondDict = {}
for x in key:
    secondDict[x] = len(value[key.index(x)])

#Create a set of the ten most populous US states
popStates = {"CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"}

#Create a new set that represents a set of populous US states that have had presidents born in them
populous = set(secondDict.keys())

combineSet = popStates.intersection(populous)
#Print a count of this new set along with an alpha-sorted listing of these states and how many presidents have been born in them.
print(f"\n{len(combineSet)} of the {len(populous)} high population states have had presidents born in them:")
for x in sorted(combineSet):
    print(x + " " + str(secondDict[x]))

'''
Execution results:
Highest population state in the Midwest is: IL 12802000

The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor

8 of the 21 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2

Process finished with exit code 0
'''