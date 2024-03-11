print('hello world')
import pandas as pd


booksDF = pd.read_excel('Modern_Library_Top_100_Best_Novels.xlsx')

print(booksDF.head())
booksDF = booksDF[['TITLE','AUTH','YEAR']]
booksDF['Available'] = True
booksDF['Reservations'] = [[] for _ in range(len(booksDF))]
booksDF['Log'] = [[] for _ in range(len(booksDF))]
print(booksDF.head)
print()
#print(booksDF[booksDF['AUTH']=='Joseph Conrad'].iloc[2].name)
test =booksDF[booksDF['AUTH']=='Joseph Conrad'].iloc[2].name
#booksDF
#print(booksDF.iloc[test])

class Library:
    def __init__(self, file):
        LibraryDF = pd.read_excel(file)
        LibraryDF = booksDF[['TITLE','AUTH','YEAR']]
        LibraryDF['Available'] = True
        LibraryDF['Reservations'] = [[] for _ in range(len(LibraryDF))]
        LibraryDF['Log'] = [[] for _ in range(len(LibraryDF))]
        
        pass
    
    
    pass


usersDF = pd.DataFrame( columns=['Name', 'Adress','Borrowed_Books','Log','Inbox'])
def newuser(df,name,adress):
    usersDF.loc[len(df)] = [name,adress,[],[],[]]
    
    
    
    
print(len(booksDF))
print(usersDF)