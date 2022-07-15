'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit F In-class assignments
'''

#---------- Part One – Using a main function, Docstrings ------------

#Write a function called hello. The function has no arguments and no return value.
# It simply prints the text "Hello World". Include a docstring that describes the function.
def hello():
  '''This function prints the text "Hello World"'''
  print("Hello World")

#---------- Part Two – Error Handling ------------

#Write a function called printListElement. The function has two arguments and no return value.
# The first argument is a list, and the second argument is a list index.
# The function will print an element from the list as determined by the list index.
# If the list index is invalid, print an error message
def printListElement(list, index):
  #Write a try block that attempts to print the list element.
  #Catch any errors with an except block, print an error message.
  try:
    print(list[index])
  except:
    print("Error: bad index number.\n")

#---------- Part Three – How Python function arguments are treated ------------

#create a function called byVal which has one argument. In the function, add 7 to the argument.
#Print the ID of the argument before and after the change.
def byVal(num):
    print(f"Original ID of parameter in byVal {id(num)}")
    num += 7
    print(f"ID of parameter in byVal after change {id(num)}")

#Create a second function called byRef which has one argument. In the function, add 7 to the last element in the list.
#Print the ID of the argument and the ID of the last element of the argument before and after the change.
def byRef(list):
    print(f"Original ID of parameter in byRef {id(list)}")
    print(f"Original ID of parameter's last element in byRef {id(list[-1])}")
    list[-1] += 7



#Write a main function, as described by the Python main function reading.
def main():
    #call hello and then print hello’s docstring.
    hello()
    print("Help on function hello in module __main__:\n")
    print("hello():\n\t" + hello.__doc__ + "\n")
    #create a myList list with elements 0, 1, 2 by using the list and range commands.
    myList = [i for i in range(0,3)]
    #call printListElement with your list and a list index value of 3.
    printListElement(myList, 3)

    #create a myInt variable and give it the value 3. Also create a myList list with elements 0, 1, 2.
    myInt = 3
    myList = [0, 1, 2]
    #print IDs of myInt and myList. Also print the ID of the last element of myList.
    print(f"Original ID of myInt in main is {id(myInt)}")
    print(f"Original ID of myList in main is {id(myList)}")
    print(f"Original ID of myList's last element in main is {id(myList[-1])}")

    #call byVal with myInt and then call byRef with myList.
    byVal(myInt)
    byRef(myList)
    #Next, again print the IDs of MyInt, myList, and the last element of myList.
    print(f"ID of parameter in byRef after change {id(myList)}")
    print(f"ID of parameter's last element in byRef after change {id(myList[-1])}")
    print(f"ID of myInt in main after call to byVal is {id(myInt)}")
    print(f"ID of myList in main after call to byRef is {id(myList)}")
    print(f"ID of myList's last element in main after call to byRef is {id(myList[-1])}")
    #Finally, print myInt and MyList from mainf
    print(f"myInt is now: {myInt}")
    print(f"myList is now: {myList}")

if __name__ == '__main__':
    main()
'''
Hello World
Help on function hello in module __main__:

hello():
	This function prints the text "Hello World"

Error: bad index number.

Original ID of myInt in main is 140714103636304
Original ID of myList in main is 2440808584200
Original ID of myList's last element in main is 140714103636272
Original ID of parameter in byVal 140714103636304
ID of parameter in byVal after change 140714103636528
Original ID of parameter in byRef 2440808584200
Original ID of parameter's last element in byRef 140714103636272
ID of parameter in byRef after change 2440808584200
ID of parameter's last element in byRef after change 140714103636496
ID of myInt in main after call to byVal is 140714103636304
ID of myList in main after call to byRef is 2440808584200
ID of myList's last element in main after call to byRef is 140714103636496
myInt is now: 3
myList is now: [0, 1, 9]

Process finished with exit code 0
'''
