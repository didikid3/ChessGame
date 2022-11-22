from PieceColor import PieceColor
class Piece:

    def __init__(self, pieceColor):
        self.pieceColor = pieceColor
        self.name = ""
        self.currentSquare = None
    

    def getName(self):
        return self.name
    
    def getPieceColor(self):
        return self.pieceColor

    def getCurrentSquare(self):
        return self.currentSquare

    def setCurrentSquare(self, currentSquare):
        self.currentSquare = currentSquare

    def __str__(self):
        res = "Piece\n"
        res += "Name - " + self.name
        res += "\nPiece Color - " + self.pieceColor.__str__()
        res += "\n" + self.currentSquare.__str__()
        res += "\n-----"
        return res