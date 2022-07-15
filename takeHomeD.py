'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit D take-home assignment
'''
from collections import namedtuple

#----- Part One - Sets -----

#Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
class1 = set()
class1.update({"Li", "Audry", "Jia", "Migel", "Tanya"})

#Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
class2 = set()
class2.update({"Sasha", "Migel", "Tanya", "Hiroto", "Audry"})

#Create a set named class3 and populate it with the students Migel, Zhang, Hiroto, Anita, Jia.
class3 = set()
class3.update({"Migel", "Zhang", "Hiroto", "Anita", "Jia"})

#Print a sorted list of students who are in all three classes.
list1 = class1.intersection(class2).intersection(class3)
print("Students in all three classes: " + str(sorted(list1)))

#Print a sorted list of all students.
list2 = class1.union(class2).union(class3)
print("All students: " + str(sorted(list2)))

#Print a sorted list of all students in class1 but not class2 or class3.
list3 = class1.difference(class2.union(class3))
print("Students in class1 but not class2 or class3: " + str(sorted(list3)))

#----- Part Two - Swap ----

#Create a list containing elements 1, 2, 3
pList = [1, 2, 3]

#Swap the second and third elements of the list. Do this with one line of code.
pList[1], pList[2] = pList[2], pList[1]
print("List after swap: " + str(pList))

#----- Part Three – Tuple Basics ----

#Create a tuple that contains the elements Casablanca, 1942, romantic drama.
movie1 = ("Casablanca", 1942, "romantic drama")

#Unpack the tuple into variables title, year, genre.
(title, year, genre) = movie1

#Print the title.
print("My favorite movie is: " + str(title))

#----- Part Four – Named Tuple ----

#Define a named tuple called Movie that contains the fields title, year, genre.
Movie = namedtuple('Movie', ['title','year','genre'])

#Create a Movie tuple that contains the elements Casablanca, 1942, romantic drama.
movie2 = Movie("Casablanca", 1942, "romantic drama")

#Print the title.
print("My favorite movie is: " + movie2.title)

#----- Part Five – Named Tuple Containing a List ----

#Define a named tuple called Moviestars that contains the fields title, year, genre, stars.
Moviestars = namedtuple('Moviestars', ['title', 'year', 'genre', 'stars'])

#Create a Moviestars tuple called favoritemovie that contains the elements Casablanca, 1942, romantic drama,
# and a list containing elements Humphrey Bogart, Ingrid Bergman.
favoritemovie = Moviestars('Casablanca', 1942, 'romantic drama', ['Humphrey Bogart', 'Ingrid Bergman'])

#Append Claude Rains to the stars list. Hint: Use the syntax favoritemovie.stars.append
favoritemovie.stars.append('Claude Rains')

#Print star Ingrid Bergman.
print("My favorite star is: " + str(favoritemovie.stars[1]))

#Print favoritemovie.
print(favoritemovie)

'''
Execution results:
Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
List after swap: [1, 3, 2]
My favorite movie is: Casablanca
My favorite movie is: Casablanca
My favorite star is: Ingrid Bergman
Moviestars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])

Process finished with exit code 0

'''