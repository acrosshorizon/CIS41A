'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit E In-class assignments
'''

#---------- First Script - Determining the genre of a movie ------------

#Create a list called scifi that contains the elements Alien, Solaris, Inception, Moon.
scifi = ["Alien", "Solaris", "Inception", "Moon"]

#Create a list called comedy that contains the elements Borat, Idiocracy, Superbad, Bridesmaids.
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"]

#Ask the user for the name of a movie.
movie = input("Please enter a movie title: ")

#Using if/elif/else, determine and print the genre of the movie.
if movie in scifi:
    print(f"{movie} is a scifi movie.")
elif movie in comedy:
    print(f"{movie} is a comedy movie.")
else:
    print(f"Sorry, I don't know what kind of movie {movie} is.")

'''
Execution results:
Please enter a movie title: Moon
Moon is a scifi movie.
Please enter a movie title: Superbad
Superbad is a comedy movie.
Please enter a movie title: Dunkirk
Sorry, I don't know what kind of movie Dunkirk is.
'''