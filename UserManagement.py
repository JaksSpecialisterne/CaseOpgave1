import pandas as pd
from User import User

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



        #Return list of book borrowed by the user
        def BorrowedBooksByUser(self):
            return not self.currentUser.borrowedBooks

        #Borrow book for user
        def UserBorrowBook(self, bookId):
            self.currentUser.BorrowBook(bookId)

        #Return book for user
        def UserReturnBook(self, bookId):
            self.currentUser.ReturnBook(bookId)

        #Check if user has book
        def UserHasBook(self, bookId):
            return self.currentUser.HasBook(bookId)



        #Log event for user, such as borrowing or returning
        def LogEvent(self, event):
            self.currentUser.LogEvent(event)



        def UserHasReservations(self):
            return not self.currentUser.NoReservation()

        def BooksReservedByUser(self):
            return self.currentUser.reservations
        
        def BookAlreadyReservedByUser(self, bookId):
            return bookId in self.currentUser.reservations



        #Initialize user from database using userId
        def LogInUser(self, userId):
            tempUser = self.users.iloc[userId]
            self.currentUser = User(userId, tempUser.NAME, tempUser.ADDRESS, tempUser.BORROWEDBOOKS, tempUser.LOG, tempUser.INBOX)

        def LogOutUser(self):
            #Gem brugere her og skriv den til dataen.
            self.currentUser = None

        #Check if id exists return.
        def UserIdExists(self, userId):
            return userId < len(self.users)
