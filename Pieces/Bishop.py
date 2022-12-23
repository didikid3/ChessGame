from Pieces.Piece import Piece
from Board import Board


class Bishop(Piece):
    

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "Bishop"

    def getValidMoves(self, board):
        print(self.getName() + "-> getValidMoves")

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")
