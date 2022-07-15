'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit F take-home assignment
'''

# Part One – Keyword Arguments and Default Values

#Write an invoice function.
#The function will generate a simple invoice and will have two required arguments and two keyword arguments.
#The two required arguments are unitPrice and quantity.
#The first keyword argument is shipping, and it has a default value of 10.
#The second keyword argument is handling, and it has a default value of 5.

def invoice(unitPrice, quantity, shipping = 10, handling = 5):
    print(f"Cost (unitPrice x quantity) = {unitPrice * quantity}")
    print(f"shipping = {shipping}")
    print(f"Handling = {handling}")
    print(f"Total = {(unitPrice * quantity) + shipping + handling}\n")

# Part Two – args (Variable-Length Arguments)

#Write a printGroupMembers function.
#The function prints a list of students who are working together on a group project, as well as the group name.
#The function has one required argument, the group name, and one variable-length argument that contains the student names.

def printGroupMembers(groupName, *studentNames):
    print(f"Members of {groupName}")
    for x in studentNames:
        print(x)

# Part Three – Non-Rectangular (Ragged) 2D lists

#The first function should be called buildBell.
#It has one argument, the number of rows, and returns a ragged table (a list of lists).
def buildBell(row):
	count = 0
	pList = []
	for r in range(row):
		sublist = []
		if r == 0:
			sublist.append(1)
			pList.append(sublist)
			count += 1
		else:
			for c in range(count + 1):
				if c == 0:
					sublist.append(pList[count - 1][-1])
				else:
					sublist.append(pList[count - 1][c - 1] + sublist[c - 1])
			pList.append(sublist)
			count += 1
	return pList

#The second function should be called printBell. It has one argument, a ragged table (a list of lists).
# Generate formatted output where each number is right justified within a fixed field size,
# so that the numbers in each column are aligned.
def printBell(list):
    for r in range(len(list)):
        for c in range(len(list[r])):
            print(str(list[r][c]).rjust(5) , end='')
        print()

def main():

    #Part one function call
    invoice(20 , 4, shipping=8)
    invoice(15, 3, handling=15)

    #Part two function call
    #First test:
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    #Second test:
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
    printGroupMembers(groupB[0] ,groupB[1] ,groupB[2] ,groupB[3] ,groupB[4])
    print()

    #Part three functions call
    triangle = buildBell(8)
    printBell(triangle)

if __name__ == '__main__':
    main()

'''
Execution results:
Cost (unitPrice x quantity) = 80
shipping = 8
Handling = 5
Total = 93

Cost (unitPrice x quantity) = 45
shipping = 10
Handling = 15
Total = 70

Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto

    1
    1    2
    2    3    5
    5    7   10   15
   15   20   27   37   52
   52   67   87  114  151  203
  203  255  322  409  523  674  877
  877 1080 1335 1657 2066 2589 3263 4140
'''
