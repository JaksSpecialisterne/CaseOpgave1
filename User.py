class User:
    def __init__(self, id, name, address, borrowedBooks = [], inbox = [], log = []):
        self.id = id
        self.name = name
        self.address = address
        self.borrowedBooks = borrowedBooks
        self.inbox = inbox
        self.log = log

    #Adds the given log to the books logs
    def AddLog(self, log):
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

    #Borrow book by book id
    def BorrowBook(self, id):
        self.borrowedBooks.append(id)

    #Return book by book id
    def ReturnBook(self, id):
        self.borrowedBooks.remove(id)

    