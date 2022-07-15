'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit J In-class assignments
'''
#                               LibraryPatron
class LibraryPatron:
    def  __init__(self,name):
        self.name = name
        self.booksCheckedOut = []

    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) < checkOutLimit:
            self.booksCheckedOut.append(bookTitle)
            print(f"{self.name} has checked out {bookTitle[0]}")
        else:
            print(f"Sorry {self.name} you are at your limit of {checkOutLimit} books")

    def returnBook(self,book):
        self.booksCheckedOut.remove(book)
        print(f"{self.name} has returned {book[0]}")


    def printCheckedOutBooks(self):
        print(f"{self.name} has the following books checked out:")
        for x in self.booksCheckedOut:
            print(x[0])

class AdultPatron(LibraryPatron):

    def  __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4

    def checkOutBook(self, book):
        super().checkOutBook(self.checkOutLimit, book)

class JuvenilePatron(LibraryPatron):

    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2

    def checkOutBook(self, book):
        if book[1] != "Juvenile":
            print(f"Sorry {book[0]} is an adult book")
        else:
            super().checkOutBook(self.checkOutLimit, book)

