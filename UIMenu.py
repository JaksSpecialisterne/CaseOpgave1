from UserManagement import UserManagement
from Library import Library
import os

userManagement = None
library = None
superSecretPassword = "password"

def ShowMenu():
    while True:
        print(f"\nWelcome {userManagement.currentUser.name}")
        print("\nSelect one:\n")
        print("1: Search for book")
        print("2: See reservations")
        print("3: See borrowed books")
        print("4: See log")
        print("5: See mailbox")
        print("6: Log out")
        input = NumberInput(1, 6)
        match input:
            case 1:
                ShowSearchMenu()
            case 2:
                ShowReservations()
            case 3:
                ShowBorrowedBooks()
            case 4:
                ShowLogs()
            case 5:
                ShowMailbox()
            case 6:
                LogOut()
                break

def ShowMenuSystem():
    while True:
        print("\nSelect one:\n")
        print("1: Log out")
        print("2: Add new book to library")
        input = NumberInput(1, 2)
        match input:
            case 1:
                break
            case 2:
                AddBookToLibrary()




def AddBookToLibrary():
    pass



def ShowBorrowedBooks():
    if userManagement.NoBorrowedByUser():
        print("\nNo borrowed books...")
    else:
        print("\nCurrent borrowed books: ")
        for book in userManagement.BorrowedBooksByUser():
            bookObject = library.getBook(book)
            print(f"{bookObject.TITLE} by {bookObject.AUTH}")
    KeyToContinue()

def ShowReservations():
    if userManagement.NoReservationsByUser():
        print("\nNo reservations...")
    else:
        print("\nCurrent resevations: ")
        for book in userManagement.ReservedBooksByUser():
            bookObject = library.getBook(book)
            print(f"{bookObject.TITLE} by {bookObject.AUTH}")
    KeyToContinue()

def ShowSearchMenu():
    print("\nHow would you like to search for your book?")
    print("1: By author\n2: by year\n3: by title\n4: By author, year or title\n5:return to menu")
    input = NumberInput(1, 5)
    if input < 5:
        SearchMenu(input)

def ShowLogs():
    print("\nLogs:")
    for log in userManagement.currentUser.log:
        print(f"{log}")
    KeyToContinue()

def ShowMailbox():
    if not userManagement.currentUser.HasMail():
        print("\nNo mail...")
    else:
        for mail in userManagement.currentUser.inbox:
            print(f"{mail}")
    KeyToContinue()



def SearchMenu(searchType):
    match searchType:
        case 1:
            method = "Author"
        case 2:
            method = "Year"
        case 3:
            method = "Title"
        case 4:
            method = ""

    difParam = False
    while True:
        searchTerm = input("\nPlease enter searchterm: ")
        if searchTerm == "retry0":
            difParam = True
            break
        LogEvent(f"Searched for term: '{searchTerm}'")
        
        if method == "":
            books = library.search(searchTerm)
        else:
            books = library.search(searchTerm, method)

        if len(books) >= 1:
            break
        print("\nNo matches found, try again, type retry0 if you wish to search by a different parameter")

    if difParam:
        ShowSearchMenu()
        return
    
    SelectBook(books)
    KeyToContinue()

def SelectBook(books):
    i = 1
    for book in books:
        print(f"{i}: {book.TITLE}, {book.AUTH}, {book.YEAR}")
        i += 1
    print("\nWhat book you wish to view more info on, reserve, unreserve, book or return\nEnter 0 to return to menu")
    input = NumberInput(0, i)-1
    if input == -1:
        return
    BookAction(books[input], books)

def BookAction(book, books):
    canReserve = not userManagement.BookAlreadyReservedByUser(book.name)
    canBorrow = CanBorrowBook(book)
    canReturn = userManagement.UserHasBook(book)
    funcToDo = []

    print(f"\nWhat would you like to do with {book.TITLE}")

    if  canReserve:
        print("1: reserve book")
        funcToDo.append(ReserveBook)
    else:
        print("1: unreserve book")
        funcToDo.append(UnreserveBook)

    if canBorrow:
        print("2: borrow book")
        funcToDo.append(BorrowBook)
    elif canReturn:
        print("2: return book")
        funcToDo.append(ReturnBook)

    print("3: return to list of books")

    input = NumberInput(1, 3)-1
    if input == 2:
        SelectBook(books)
    else:
        funcToDo[input](book)
    


def CanBorrowBook(book):
    if len(book.RESERVATIONS) > 0:
        if book.RESERVATIONS[0] == userManagement.currentUser.userId:
            return book.AVAILABLE
        else:
            return False
    else:
        return book.AVAILABLE

def BorrowBook(book):
    bookId = book.name
    userManagement.UserBorrowBook(bookId)
    library.changeAvailability(bookId, userManagement.currentUser.userId)
    SaveBookToFile(bookId)
    print(f"You have borrowed {book.TITLE}")

def ReturnBook(book):
    bookId = book.name
    userManagement.UserReturnBook(bookId)
    library.changeAvailability(bookId, userManagement.currentUser.userId)
    SaveBookToFile(bookId)
    print(f"You have returned {book.TITLE}")
    NotifyReservers()

def ReserveBook(book):
    bookId = book.name
    userManagement.UserReserveBook(bookId)
    library.newReserve(bookId, userManagement.currentUser.userId)
    SaveBookToFile(bookId)
    print(f"You have reserved {book.TITLE}")

def UnreserveBook(book):
    bookId = book.name
    userManagement.UserUnreserveBook(bookId)
    library.removeReservation(bookId, userManagement.currentUser.userId)
    SaveBookToFile(bookId)
    print(f"You have unreserved {book.TITLE}")



def SaveBookToFile(bookId):
    library.WriteToExcel(library.filename, bookId)

def NotifyReservers(book):
    #userManagement.NotifyUsers(book)
    pass

def LogEvent(event):
    userManagement.LogEvent(event)



def NumberInput(minNum, maxNum):
    while True:
        num = input("\nPlease enter a number ")
        try:
            val = int(num)
            if val <= maxNum and val >= minNum:
                return val
            else:
                print("Not a valid number...")
        except ValueError:
            print("Not a number...")

def KeyToContinue():
    print("\nPress a key to continue...")
    input()
    os.system('cls')

def SystemLogIn():
    SystemLogOn = False
    while True:
        passw = input("\nPlease enter the system password or return0 to return to login screen ")
        global superSecretPassword
        if passw == superSecretPassword:
            SystemLogOn = True
            break
        elif passw == "return0":
            break

    if SystemLogOn:
        ShowMenuSystem()

def LogInMenu():
    os.system('cls')
    userManagement.ReadExcelFile()
    userAmount = len(userManagement.users)
    while True:
        print("\nPlease enter your userId")
        num = input()
        try:
            val = int(num)
            if val >= 0 and val < userAmount:
                userManagement.LogInUser(val)
                break
            else:
                print("\nNot a valid userId...")
        except ValueError:
            print("\nMust be a number...")
    return

def LogOut():
    userManagement.LogOutUser()

def StartMenu():
    while True:
        os.system('cls')
        print("1: Log into user")
        print("2: Log into system library")
        print("3: Close system")
        input = NumberInput(1, 3)
        match input:
            case 1:
                LogInMenu()
                KeyToContinue()
                ShowMenu()
            case 2:
                SystemLogIn()
            case 3:
                break

def Initialize():
    global userManagement
    userManagement = UserManagement()
    global library
    library = Library()

if __name__ == '__main__':
    Initialize()
    StartMenu()