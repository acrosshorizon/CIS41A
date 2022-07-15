'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit C take-home assignment
'''
import copy

#---------- First Script - Working with Lists ------------
#Create an empty list called list1
list1 = []
#Populate list1 with the values 1,3,5
x = 0
while x < 3:
    list1.append(2*x + 1)
    x += 1
#Create list2 and populate it with the values 1,2,3,4
list2 = []
x = 1
while x <= 4:
    list2.append(x)
    x += 1
#Create list3 by using + (a plus sign) to combine list1 and list2. Print list3.
list3 = list1 + list2
print("list3 is: " + str(list3))
#Use sequence operator in to test list3 to see if it contains a 3, print True/False result (do with one line of code).
print("list3 contains a 3: " + str(3 in list3))
#Count the number of 3s in list3, print the result.
print(f"{'list3 contains':2}{list3.count(3):>2}{'3s':>3}")
#Determine the index of the first 3 in list3, print the result.
print("The index of the first 3 contained in list3 is " +str(list3.index(3)))
#Pop this first 3 and assign it to a variable called first3, print first3.
first3 = list3[list3.index(3)]
list3.pop(list3.index(3))
print("first3 = " +str(first3))
#Create list4, populate it with list3's sorted values, using the sorted built-in function
list4 = copy.deepcopy(list3)
list4.sort()
#Print list3 and list4
print("list3 is now: " +str(list3))
print("list4 is: " + str(list4))
#Slice list3 to obtain a list of the values 1,2,3 from the middle of list3, print the result.
slice_obj = slice(2,5,1)
print("Slice of list3 is: "+ str(list3[slice_obj]))
#Determine the length of list3, print the result.
print("Length of list3 is " +str(len(list3)))
#Determine the max value of list3, print the result.
print("The max value in list3 is " +str(max(list3)))
#Sort list3 (use the list sort method), print list3.
list3.sort()
print("orted list3 is: " + str(list3))
#Create list5, a list of lists, using list1 and list2 as elements of list5, print list5.
list5 = [list1, list2]
print("list5 is: " + str(list5))
#Print the value 4 contained within list5.
print("Value 4 from list5: " + str(list5[1][3]))

'''
list3 is: [1, 3, 5, 1, 2, 3, 4]
list3 contains a 3: True
list3 contains 2 3s
The index of the first 3 contained in list3 is 1
first3 = 3
list3 is now: [1, 5, 1, 2, 3, 4]
list4 is: [1, 1, 2, 3, 4, 5]
Slice of list3 is: [1, 2, 3]
Length of list3 is 6
The max value in list3 is 5
orted list3 is: [1, 1, 2, 3, 4, 5]
list5 is: [[1, 3, 5], [1, 2, 3, 4]]
Value 4 from list5: 4

Process finished with exit code 0

'''