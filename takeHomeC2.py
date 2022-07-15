'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit C take-home assignment
'''

#---------- Second Script - Bit Operators ------------
#Assign the values 9 and 14 to variables a and b respectively.
a = 9
b = 14
#Print the binary values of a and b (use the bin built-in function).
print("binary of a = " +  str(bin(a)))
print("binary of b = " + str(bin(b)))
#Calculate the value of a and b, print the result in binary.
andBit = a & b
print("binary of a & b =  " + str(bin(andBit)))
#Calculate the value of a or b, print the result in binary.
orBit = a | b
print("binary of a | b =  " + str(bin(orBit)))

'''
Execution results:

binary of a = 0b1001
binary of b = 0b1110
binary of a & b =  0b1000
binary of a | b =  0b1111
'''