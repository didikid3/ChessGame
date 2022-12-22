from Pieces.Piece import Piece
from Board import Board

class Pawn(Piece):

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "Pawn"

    def getValidMoves(self, board, square=None):
        print(self.getName() + "-> getValidMoves")

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")