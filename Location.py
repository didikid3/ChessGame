from File import File

class Location:
    
    def __init__(self, file, rank):
        self.__file = File(file)
        self.__rank = rank

    
    def getFile(self):
        return self.__file
    def getRank(self):
        return self.__rank

    
    def equals(self, other):
        if self == other:
            return True

        if type(other) is not type(self):
            return False
        
        return self.__file == other.getFile() \
            and self.__rank == other.getRank()

    
    def __str__(self):
        return self.__file.__str__() + " " + str(self.__rank)
    