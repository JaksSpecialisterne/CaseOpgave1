from UserManagement import UserManagement
import os

userManagement = None


#Shows menu for the user
def ShowMenu():
    print("\nSelect one:\n")
    print("1: Log out")
    print("2: Search for book")
    print("3: See reservations")
    print("4: See borrowed books")
    #print("5: See borrowed book history")
    numOptions = 5
    input = NumberInput(numOptions)
    match input:
        case 1:
            LogOut()
        case 2:
            ShowSearchMenu()
        case 3:
            ShowReservations()
        case 4:
            ShowBorrowedBooks()
        #case 5:
            #pass

def ShowBorrowedBooks():
    #Check if any reservations
    if userManagement.BorrowedBooksByUser():
        print("No borrowed books...")
    else:
        print("Current borrowed books: ")
        for i in userManagement.BorrowedBooksByUser:
            print("Book: " + "book stuff here")
    KeyToContinue()
    ShowMenu()

def ShowReservations():
    #Check if any reservations
    if userManagement.UserHasReservations():
        print("No reservations...")
    else:
        print("Current resevations: ")
        for i in userManagement.BookReservedByUser:
            print("Book: " + "book stuff here")
    KeyToContinue()
    ShowMenu()

def ShowSearchMenu():
    print("How would you like to search for your book?")
    print("1: By author\n2: by year\n3: by title")
    input = NumberInput(3)
    SearchMenu(input)



#Show menu for search along, depending on choice it calls one of the functions below
def SearchMenu(searchType):
    searchTerm = input("Please enter searchterm: ")
    match searchType:
        case 1:
            books = []
            pass#Library.SearchAuthor(searchTerm)
        case 2:
            books = []
            pass#Library.SearchYear(searchTerm)
        case 3:
            books = []
            pass#Library.SearchTitle(searchTerm)
    SelectBook(books)


def SelectBook(books):
    i = 0
    for book in books:
        print(i + ": " + book.TITLE + ", " + book.AUTHOR + ", " + book.YEAR)
        i += 1
    input = NumberInput(i)
    ReserveOrBorrow(books[i])

def ReserveOrBorrow(book):
    i = 1
    if book.AVAILABLE:
        print(i + ": borrow book")
        i += 1
        #stuff to borrow
    if  userManagement.BookAlreadyReservedByUser(book.name):
        print(i + ": reserve book")
        #stuff to reserve



def NumberInput(maxNum):
    while True:
        num = input("Please enter a number ")
        try:
            val = int(num)
            if val <= maxNum and val > 0:
                return val
            else:
                print("Not a valid number...")
        except ValueError:
            print("Not a number...")

def KeyToContinue():
    print("press a key to continue...")
    input()
    os.system('cls')

def LogInMenu():
    os.system('cls')
    userAmount = 100#sæt den til at være størrelsen af usert database - 1
    while True:
        num = input("Please enter your userId ")
        try:
            val = int(num)
            maxUser = 10
            if val <= maxUser and val >= 0:
                #Sæt curren user i management her
                userManagement.LogInUser(val)
                ShowMenu()
            else:
                print("Not a valid userId...")
        except ValueError:
            print("Not a userId, must be a integer...")

def LogOut():
    #Sæt current user i user managedment til None
    LogInMenu()

if __name__ == '__main__':
    #Initialise library and user management here
    userManagement = UserManagement()
    LogInMenu()