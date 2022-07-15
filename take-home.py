'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit B In-class assignments
'''

#----- String methods -----

#Ask the user for a name (test with George Washington).
name = input("Enter a name: ")
#Print the name in all uppercase letters.
print(name.upper())
#Print the length of the name.
print("Length: " + str(len(name)))
#Print the 4th character of the name (r).
print("4th character: "+ name[3])
#Create a variable called name2. Assign to name2 the name with all "o" characters replaced with "x"s.
name2 = name.replace('o','x')
#Print name2.
print("name2: "  +str(name2))
#Print the original name.
print("Original name: " +str(name) + "\n")

#----- Counting and Finding -----

#Assign the text "Believe you can and you're halfway there." to a variable called quote (this is a quote from Theodore Roosevelt).
quote = "Believe you can and you're halfway there."
#Count how many "a" characters there are, print the result.
count = 0
a = 0
while a < len(quote):
    if quote[a] == 'a':
        count += 1
    a += 1
print("how many \"a\" characters there are: " + str(count))

#Print the index of all the "a" characters.
x = 0
i = 0
while i < count:
    if x == 0:
        x = quote.find('a')
    else:
        x = quote.find('a',x + 1,len(quote))
    print("a founded at index: " + str(x))
    i += 1

'''
Execution results:
Enter a name: George Washington
GEORGE WASHINGTON
Length: 17
4th character: r
name2: Gexrge Washingtxn
Original name: George Washington

how many "a" characters there are: 4
a founded at index: 13
a founded at index: 16
a founded at index: 28
a founded at index: 32
'''