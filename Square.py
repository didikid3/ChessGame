from SquareColor import SquareColor
from Location import Location

class Square:

    def __init__(self, color, location, occupied=False):
        self.__squareColor = color
        self.__location = location
        self.__isOccupied = occupied

    
    def reset(self):
        self.__isOccupied = False

    
    def isOccupied(self):
        return self.__isOccupied

    def setOccupied(self, occupied):
        self.__isOccupied = occupied

    def getSquareColor(self):
        return self.__squareColor

    def setSquareColor(self, color):
        self.__squareColor = color
    
    def getLocation(self):
        return self.__location
    
    def setLocation(self, location):
        self.__location = location

    def __str__(self):
        res = "---------\nSquare"
        res += "\nColor - " + self.__squareColor.__str__()
        res += "\nLocation - " + self.__location.__str__()
        res += "\nOccupied - " + str(self.__isOccupied)
        res += "\n--------\n"

        return res