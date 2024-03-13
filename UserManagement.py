import pandas as pd
from User import User
from datetime import datetime
import ast

class UserManagement:
    __instance  = None
    def  __init__(self):
        if UserManagement.__instance is None:
            UserManagement.__instance = UserManagement.__impl()  
        #self.__dict__['_DataFrame_instance'] = DataFrame.__instance
        
    #redirects any function calls to the inner class __impl
    def __getattr__(self, attr):
        return getattr(self.__instance, attr)
    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)
    
    #Actual code goes in this inner class
    class __impl:
        def __init__(self):
            self.users = pd.read_excel('user_data.xlsx')
            self.currentUser = None

        #Adds user to the database of users
        def AddUser(self, name, address):
            self.users.loc[len(self.users)] = [name, address, [], [], []]

        #Notify user who has reservation for given book by id
        def NotifyUsers(self, userId, mail):
            self.users.iloc[userId].INBOX.append(mail)



        #Borrow book for user
        def UserBorrowBook(self, bookId):
            self.currentUser.BorrowBook(bookId)
            self.LogEvent(f"Borrowed book with id: {bookId} at {self.GetTimeStamp()}")

        #Return book for user
        def UserReturnBook(self, bookId):
            self.currentUser.ReturnBook(bookId)
            self.LogEvent(f"Returned book with id: {bookId} at {self.GetTimeStamp()}")

        #Reserves Book
        def UserReserveBook(self, bookId):
            self.currentUser.ReserveBook(bookId)
            self.LogEvent(f"Reserved book with id: {bookId} at {self.GetTimeStamp()}")

        #Unreserve Book
        def UserUnreserveBook(self, bookId):
            self.currentUser.UnreserveBook(bookId)
            self.LogEvent(f"Unreserved book with id: {bookId} at {self.GetTimeStamp()}")



        #Check if user has book
        def UserHasBook(self, book):
            return self.currentUser.HasBook(book.name)

        #Return list of books borrowed by the user
        def BorrowedBooksByUser(self):
            return self.currentUser.borrowedBooks
        
        #Return list of books reserved by the user
        def ReservedBooksByUser(self):
            return self.currentUser.reservations

        #Check if user has any reservations
        def NoReservationsByUser(self):
            return self.currentUser.NoReservation()
        
        #Check if user has any reservations
        def NoBorrowedByUser(self):
            return self.currentUser.NoBorrowedBooks()
        
        #Checks if book is already reserved by user
        def BookAlreadyReservedByUser(self, bookId):
            return bookId in self.currentUser.reservations



        def GetTimeStamp(self):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            return current_time

        #Log event for user, such as borrowing or returning
        def LogEvent(self, event):
            self.currentUser.LogEvent(event)

        #Initialize user from database using userId
        def LogInUser(self, userId):
            tempUser = self.users.iloc[userId]
            #self.currentUser = User(userId, tempUser.NAME, tempUser.ADDRESS, tempUser.BORROWEDBOOKS, tempUser.LOG, tempUser.INBOX)
            self.currentUser = User(userId, tempUser.NAME, tempUser.ADDRESS, ast.literal_eval(tempUser.BORROWEDBOOKS), ast.literal_eval(tempUser.LOG) ,ast.literal_eval(tempUser.INBOX))
            self.LogEvent("Log in at " + self.GetTimeStamp())

        def LogOutUser(self):
            #Gem brugere her og skriv den til dataen.
            self.LogEvent("Log out at " + self.GetTimeStamp())
            self.currentUser = None

        #Check if id exists return.
        def UserIdExists(self, userId):
            return userId < len(self.users)
