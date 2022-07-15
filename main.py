'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit D In-class assignments
'''
import copy
#######################################################
#----------------Dictionary Basics---------------------
#######################################################

#Create a dictionary of fruit and desserts made from the fruit.
#The fruit should be the key and the dessert should be the value. Use these key value pairs:
#apple:sauce
#peach:cobbler
#carrot:cake
#strawberry:sorbet
#banana:cream pie
fruitDict = {
    "apple" : "sauce",
    "peach" : "cobbler",
    "carrot" : "cake",
    "strawberry" : "sorbet",
    "banana" : "cream pie"
}

#Add the mango fruit to the dictionary. Its dessert is sticky rice.
fruitDict["mango"] = "sticky rice"

#Change the strawberry dessert to shortcake.
fruitDict.update({"strawberry" : "shortcake"})

#Carrot is not a fruit, so remove carrot from the dictionary.
fruitDict.pop("carrot")

#Print the apple dessert.
print("apple dessert is: " + fruitDict["apple"])

#See if a banana dessert exists.
print("banana dessert exists: " + str("banana" in fruitDict))

#See if a pear dessert exists.
print("pear dessert exists: " + str("pear" in fruitDict))

#Print the keys in the dessert dictionary.
print(fruitDict.keys())

#Print the values in the dessert dictionary.
print(fruitDict.values())

#Print the key-value pairs in the dessert dictionary.
print(fruitDict.items())

#######################################################
#----------------Combining dictionaries----------------
#######################################################

#Create a dictionary named capitols1 and populate it with these key value pairs:
#Alabama:Montgomery
#Alaska:Juneau
#Arizona:Phoenix
#Arkansas:Little Rock
#California:Sacramento
capitols1 = {
    "Alabama" : "Montgomery",
    "Alaska" : "Juneau",
    "Arizona" : "Phoenix",
    "Arkansas" : "Little Rock",
    "California" : "Sacramento"
}

#Create a dictionary named capitols2 and populate it with these key value pairs:
#California:Sac.
#Colorado:Denver
#Connecticut:Hartford
capitols2 = {
    "California" : "Sac." ,
    "Colorado" : "Denver",
    "Connecticut" : "Hartford"
}

#Using the dictionary update() method, update capitols1 with capitols2.
capitols1.update(capitols2)

#Print the sorted capitols (values). Note the updated value of California's capitol.
print("Sorted state capitols: " + str(sorted(capitols1.values())))

#######################################################
#----------------Sets Basics---------------------------
#######################################################

#Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}

#Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}

#Add John to class1.
class1.add("John")

#Print a sorted list of students who are in both classes.
print("Students in both classes:" +str(sorted(class1.intersection(class2))))

#Print a sorted list of all students.
print("All students: " + str(sorted(class1.union(class2))))

#Test to see if Sasha is in class1.
print("Sasha is in class1: " + str("Sasha" in class1))
'''
apple dessert is: sauce
banana dessert exists: True
pear dessert exists: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
Sorted state capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes:['Audry', 'Migel', 'Tanya']
All students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1: False

Process finished with exit code 0

'''



