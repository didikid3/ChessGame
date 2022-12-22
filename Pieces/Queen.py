from Board import Board
from Pieces.Piece import Piece

class Queen(Piece):

    def __init__(self, pieceColor, bishop, rook):
        Piece.__init__(self, pieceColor)
        self.bishop = bishop
        self.rook = rook
        self.name = "Queen"

    def getValidMoves(self, board, square=None):
        moveCandidates = []
        moveCandidates.extend(self.bishop.getValidMoves(board, self.getCurrentSquare()))
        moveCandidates.extend(self.rook.getValidMoves(board, self.getCurrentSquare()))
        
        return moveCandidates

    def makeMove(self, square):
        current = self.getCurrentSquare()
        self.setCurrentSquare(square)
        current.reset()