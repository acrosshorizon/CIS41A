'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit B take-home assignment
'''

#---------- First Script - Working with Strings ------------

#-------------- String Type Tests -------------------------
#Ask the user for a string (test with "ABC123").
data = input("Enter a String: ")
#Use method isupper to test the string, print the result.
print("All characters in the string are upper case: " + str(data.isupper()))
#Use method isdigit to test the string, print the result.
print("All characters in the string are digits: "+ str(data.isdigit()))
#Use method isalpha to test the string, print the result.
print("All characters in the string are in the alphabet: " + str(data.isalpha()))
#-----------------------------------------------------------

#---------- Escape Characters within a string --------------
#Assign the text "Type, type, type away. Compile. Run.
# Hip hip hooray! No error today!" to a single variable (be sure to add newline escape characters).
# This should be done in a single line of code.
txt = "Type, type, type away.\nCompile. Run. Hip hip hooray!\nNo error today!\n"
print(txt)
#-----------------------------------------------------------

#---------- Slicing a string -------------------------------
#Assign the text "And now for something completely different" to a variable called quote.
quote = "And now for something completely different"
#Slice quote to obtain the text "And no" from the beginning of the quote, print the results.
print(quote[0:6])
#Slice quote to obtain the text "rent" from the end of the quote, print the results.
print(quote[-4:])
#Slice quote to obtain the text "me" from the middle of the quote, print the results.
print(quote[14:16])
#Slice quote to obtain the text "Adnwf..." by extracting every other letter, print the results.
print(quote[0::2])
#Slice quote to obtain the text "tnere..." by reversing the quote, print the results.
print(quote[::-1])
#-----------------------------------------------------------

#-------------- Using string operators + and * ---------------
#Assign the text ".~*'" to a variable called pattern1.
pattern1 = ".~*'"
#Create a variable called pattern2, assign to it pattern1 combined with pattern1 reversed.
# pattern2 should now contain the string ".~*''*~."
pattern2 = pattern1 + pattern1[::-1]
#Print pattern2 repeated five times.
print(pattern2*5)
#-----------------------------------------------------------

'''
Enter a String: ABC123
All characters in the string are upper case: True
All characters in the string are digits: False
All characters in the string are in the alphabet: False
Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!

And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.

Process finished with exit code 0
'''

