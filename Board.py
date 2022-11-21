from File import File
from Location import Location
from SquareColor import SquareColor
from Square import Square

class Board:

    def __init__(self) :
        self.boardSquares = [ [None for x in range(8)] for y in range(8)]

        for i in range(8):
            col = 0
            currColor = "Light" if i%2 == 0 else "Dark"
            file = 'A'

            for j in range(8):
                squareColor = SquareColor(currColor)
                location = Location(file, 8-i)

                self.boardSquares[i][col] = Square(squareColor, location)

                #Update Per Square
                file = chr(ord(file) + 1)
                col += 1
                currColor = "Light" if (currColor == "Dark") else "Dark"


    def printBoard(self):
        for row in self.boardSquares:
            for square in row:
                print(square, end="")
            print()
        
                