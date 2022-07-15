'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit I take-home assignment
'''

# Part 1 of 1 Inheritance with Multiple Children
class LibraryPatron:
    #The __init__ method should have the parameters self and name, and should store the name as an attribute
    #(name is the name of the patron).
    #There should also be an additional attribute called booksCheckedOut which should be initialized as an empty list.
    #This attribute will store a list of the book titles that the patron currently has checked out.
    def  __init__(self,name):
        self.name = name
        self.booksCheckedOut = []

    #The checkOutBook method should have the parameters self, checkOutLimit and bookTitle. If the patron is at their checkout limit,
    #print a "Sorry" message to the patron.
    #Otherwise, append the bookTitle to the patron's booksCheckedOut list and print a "Checkout" message.
    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) < checkOutLimit:
            self.booksCheckedOut.append(bookTitle)
            print(f"{self.name} has checked out {bookTitle[0]}")
        else:
            print(f"Sorry {self.name} you are at your limit of {checkOutLimit} books")

    #The returnBook method should have the parameters self and book.
    #Remove the book title from the patron's list of checked out book titles and print a "returned" message.
    def returnBook(self,book):
        self.booksCheckedOut.remove(book)
        print(f"{self.name} has returned {book[0]}")

    #The printCheckedOutBooks method should have the parameter self.
    #Print a message along and print all the patron's checked out book title
    def printCheckedOutBooks(self):
        print(f"{self.name} has the following books checked out:")
        for x in self.booksCheckedOut:
            print(x[0])

class AdultPatron(LibraryPatron):
    #The __init__ method should have the parameters self and name. Call LibraryPatron's __init__ to store the name.
    #There should also be an additional attribute called checkOutLimit which should be initialized with a value of 4.
    def  __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4

    #The checkOutBook method should have the parameters self and book. Here again, book is a book list object.
    #Call LibraryPatron's checkOutBook method, using the patron's checkOutLimit and the book title as arguments.
    def checkOutBook(self, book):
        super().checkOutBook(self.checkOutLimit, book)

class JuvenilePatron(LibraryPatron):
    #The __init__ method should have the parameters self and name. Call LibraryPatron's __init__ to store the name.
    #There should also be an additional attribute called checkOutLimit which should be initialized with a value of 2.
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2

    #The checkOutBook method should have the parameters self and book.
    #If the book is not a a juvenile book, print a "Sorry" message as shown below
    #Otherwise, call LibraryPatron's checkOutBook method, using the patron's checkOutLimit and the book title as arguments.
    def checkOutBook(self, book):
        if book[1] != "Juvenile":
            print(f"Sorry {book[0]} is an adult book")
        else:
            super().checkOutBook(self.checkOutLimit, book)

def main():
    book1 = ["Alice in Wonderland", "Juvenile"]
    book2 = ["The Cat in the Hat", "Juvenile"]
    book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
    book4 = ["The Hobbit", "Juvenile"]
    book5 = ["The Da Vinci Code", "Adult"]
    book6 = ["The Girl with the Dragon Tattoo", "Adult"]

    patron1 = JuvenilePatron("Jimmy")
    patron2 = AdultPatron("Sophia")

    patron1.checkOutBook(book6)
    patron1.checkOutBook(book1)
    patron1.checkOutBook(book2)
    patron1.printCheckedOutBooks()
    patron1.checkOutBook(book3)
    patron1.returnBook(book1)
    patron1.checkOutBook(book3)
    patron1.printCheckedOutBooks()
    patron2.checkOutBook(book5)
    patron2.checkOutBook(book4)
    patron2.printCheckedOutBooks()

if __name__ == '__main__':
    main()

'''
Execution results:
Sorry The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2 books
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit
'''