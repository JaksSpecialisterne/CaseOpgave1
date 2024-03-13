import pandas as pd
import ReadFile
import numpy as np




class Library:
    #################    
    ### SINGLETON ###
    #################
    # initialisation checks for instance and only initialises the actual object if there are no other instances
    __instance  = None
    def  __init__(self):
        if Library.__instance is None:
            Library.__instance = Library.__impl()  
        #self.__dict__['_DataFrame_instance'] = DataFrame.__instance
        
    #redirects any function calls to the inner class __impl
    def __getattr__(self, attr):
        return getattr(self.__instance, attr)
    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)
    
    #Actual code goes in this inner class
    class __impl:
        def __init__(self):
            pass
        LibDF = ReadFile.ReadFile().data
        
        def searchTitle(self,_input):
            sNresults = []
            for i in range(len(self.LibDF)):
                #print(self.LibDF.iloc[i])
                if _input in self.LibDF.iloc[i].TITLE: # == _input:
                    sNresults.append(self.LibDF.iloc[i])
            return(sNresults)
            pass
        
        def searchAuthor(self,_input):
            sAresults = []
            for i in range(len(self.LibDF)):
                #print(self.LibDF.iloc[i])
                if _input in self.LibDF.iloc[i].AUTH: #== _input:
                    sAresults.append(self.LibDF.iloc[i])
            return(sAresults)
            pass
        
        def searchYear(self,_input):
            sYresults = []
            
            for i in range(len(self.LibDF)):
                #print(self.LibDF.iloc[i].YEAR)
                #print(self.LibDF.iloc[i])
                if str(_input) in str(self.LibDF.iloc[i].YEAR): # == _input:
                    sYresults.append(self.LibDF.iloc[i])
            return(sYresults)
            pass
        
        def search(self,method, _input):
            if method == 'Title':
                return self.searchTitle(_input)
            elif method == 'Author':
                return self.searchAuthor(_input)
            elif method == 'Year':
                return self.searchYear(_input)
            else:
                print('ERROR! Unknown method passed to search function: '+str(method))
            
            
            pass
        
        
        
        def getIndex(self,method, _input):
            gI_search = self.search(method, _input)
            if len(gI_search) >= 1:
                return gI_search[0].name
            else:
                print('ERROR! No search results for ' + str(_input)+' in getIndex function of library class object.')
            pass
        
        def changeAvailability(self,index):
            #print(self.LibDF['AVAILABLE'][index])
            self.LibDF.loc[index,('AVAILABLE')] = not self.LibDF.loc[index,('AVAILABLE')]
            
            
        def newLog(self, index, _log):
            self.LibDF.loc[index,('LOG')].append(_log)
            
            pass
        
        def newReserve(self, index, _reservation):
            self.LibDF.loc[index,('RESERVATIONS')].append(_reservation)
            
        def removeReservation(self, bookID, userID):
            rR_removals = []
            for i in range(len( self.LibDF['RESERVATIONS'][bookID])):
                if self.LibDF['RESERVATIONS'][bookID][i] == userID:
                    rR_removals.append(i)
            rR_removals = np.array(rR_removals)
            for j in rR_removals:
                self.LibDF['RESERVATIONS'][bookID].pop(j)
                rR_removals -=1
            pass
        
        def isReservedBy(self,bookID,userID):
            if userID in self.LibDF['RESERVATIONS'][bookID]:
                return True
            else:
                return False


        # Test function to check ID
        def spam(self):
            return id(self)
    pass

check = Library()
#print(check.LibDF.head())

print(check.search('Year','197'))

#check.newReserve(0,156)
#check.newReserve(0,12)
#check.newReserve(0,9000)
#check.removeReservation(0,156)
#check.removeReservation(0,9000)
#check.removeReservation(0,12)
print(check.LibDF.head())
print(check.getIndex('Year',1899))
print(check.isReservedBy(0,156))
#print(len(booksDF))
#print(usersDF)