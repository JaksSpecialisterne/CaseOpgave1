import pandas as pd
import ReadFile




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
                if self.LibDF.iloc[i].TITLE == _input:
                    sNresults.append(self.LibDF.iloc[i])
            return(sNresults)
            pass
        
        def searchAuthor(self,_input):
            sAresults = []
            for i in range(len(self.LibDF)):
                #print(self.LibDF.iloc[i])
                if self.LibDF.iloc[i].AUTH == _input:
                    sAresults.append(self.LibDF.iloc[i])
            return(sAresults)
            pass
        
        def searchYear(self,_input):
            sYresults = []
            for i in range(len(self.LibDF)):
                #print(self.LibDF.iloc[i])
                if self.LibDF.iloc[i].YEAR == _input:
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
        
        def changeAvailability(self,index):
            #print(self.LibDF['AVAILABLE'][index])
            self.LibDF.loc[index,('AVAILABLE')] = not self.LibDF.loc[index,('AVAILABLE')]
            
            
        def newLog(self, index, _log):
            self.LibDF.loc[index,('LOG')].append(_log)
            
            pass
        
        def newReserve(self, index, _reservation):
            self.LibDF.loc[index,('RESERVATIONS')].append(_reservation)

        # Test function to check ID
        def spam(self):
            return id(self)
    pass

check = Library()
#print(check.LibDF.head())

#print(check.search('Year',1925))


    

print(check.LibDF.head())
#print(len(booksDF))
#print(usersDF)