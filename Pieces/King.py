from Pieces.Piece import Piece
from Board import Board

class King(Piece):

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "King"

    def getValidMoves(self):
        print(self.getName() + "-> getValidMoves")
        cur_row = self.getCurrentSquare()[0]
        cur_col = self.getCurrentSquare()[1]
        color = self.getPieceColor()
        

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")