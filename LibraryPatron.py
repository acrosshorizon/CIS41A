'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit J In-class assignments
'''
#                   LibraryPatron
class LibraryPatron:
    def  __init__(self,name):
        self.name = name
        self.booksCheckedOut = []

    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) < checkOutLimit:
            self.booksCheckedOut.append(bookTitle)
            print(f"{self.name} has checked out {bookTitle}")
        else:
            print(f"Sorry {self.name} you are at your limit of {checkOutLimit} books")

    def returnBook(self,book):
        title = book.title
        self.booksCheckedOut.remove(title)
        print(f"{self.name} has returned {book.title}")


    def printCheckedOutBooks(self):
        print(f"{self.name} has the following books checked out:")
        for x in self.booksCheckedOut:
            print(x)

class AdultPatron(LibraryPatron):

    def  __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4

    def checkOutBook(self, book):
        super().checkOutBook(self.checkOutLimit, book.title)

class JuvenilePatron(LibraryPatron):

    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2

    def checkOutBook(self, book):
        if book.bookType != "Juvenile":
            print(f"Sorry {book.title} is an adult book")
        else:
            super().checkOutBook(self.checkOutLimit, book.title)


