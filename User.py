class User:
    def __init__(self, userId, name, address, borrowedBooks = [], reservations = [], inbox = [], log = []):
        self.userId = userId
        self.name = name
        self.address = address
        self.borrowedBooks = borrowedBooks
        self.reservations = reservations
        self.inbox = inbox
        self.log = log

    #Adds the given log to the books logs
    def LogEvent(self, log):
        self.log.append(log)

    #Adds mail to the user
    def RecieveMail(self, mail):
        self.inbox.append(mail)

    #Check whether the user has any mail
    def HasMail(self):
        return not (not self.inbox)

    #Remove all mails from user
    def RemoveAllMail(self):
        self.inbox = []

    #Borrow book by bookId
    def BorrowBook(self, bookId):
        self.borrowedBooks.append(bookId)

    #Return book by bookId
    def ReturnBook(self, bookId):
        self.borrowedBooks.remove(bookId)

    def HasBook(self, bookId):
        return bookId in self.borrowedBooks
    
    def NoReservation(self):
        return not self.reservations

    