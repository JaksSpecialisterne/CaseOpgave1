import enum
import Library

class SearchType (enum):
    AUTHOR = 1
    YEAR = 2
    TITLE = 3

#Shows menu for the user
def ShowMenu(userID):
    pass

#Show menu for search along, depending on choice it calls one of the functions below
def SearchMenu(searchType, searchTerm):
    match searchType:
        case SearchType.AUTHOR:
            Library.SearchAuthor(searchTerm)
        case SearchType.YEAR:
            Library.SearchYear(searchTerm)
        case SearchType.TITLE:
            Library.SearchTitle(searchTerm)

#Move next three to libraryt class instead
#Searches for book by author
def SearchAuthor(searchTerm):
    pass

#Searches for book by year
def SearchYear(searchTerm):
    pass

#Searches for book by title
def SearchTitle(searchTerm):
    pass
#
#

def LogInMenu():
    pass

def LogOut():
    pass
