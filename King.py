from Movable import Movable
from Piece import Piece
from Board import Board
from Square import Square

class King(Piece, Movable):

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "King"

    def getValidMoves(self, board, square=None):
        print(self.getName() + "-> getValidMoves")

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")