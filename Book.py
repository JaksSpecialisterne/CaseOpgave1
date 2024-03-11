class Book:
    def __init__(self, id, title, author, year, available = True, reservations = [], log = []):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.reservations = reservations
        self.log = log
    
    #Switches availability of book
    def ChangeAvailableStatus(self):
        self.available = not self.available

    #Adds the given log to the books logs
    def AddLog(self, log):
        self.log.append(log)

    #Adds the specified user id to the reservations
    def AddReservation(self, id):
        self.reservations.append(id)

    #Removes either the first reservation on the book or the reservation for the given user id
    def RemoveReservation(self, id = -1):
        if id == -1:
            self.reservations.pop(0)
        else:
            self.reservations.remove(id)

    #Checks whether the book is reserved
    def NotReserved(self):
        return not self.reservations