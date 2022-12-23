from Pieces.Piece import Piece
from Board import Board

class Knight(Piece):

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "Knight"

    def getValidMoves(self, board):
        print(self.getName() + "-> getValidMoves")

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")