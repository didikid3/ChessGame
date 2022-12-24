from Board import Board
from Pieces.Piece import Piece
from Pieces.Bishop import Bishop
from Pieces.Rook import Rook

class Queen(Piece):

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.bishop = Bishop(pieceColor)
        self.rook = Rook(pieceColor)
        self.name = "Queen"

    def setCurrentSquare(self, currentSquare):
        self.currentSquare = currentSquare
        self.bishop.setCurrentSquare(currentSquare)
        self.rook.setCurrentSquare(currentSquare)

    def getValidMoves(self):
        moveCandidates = []
        moveCandidates.extend(self.bishop.getValidMoves())
        moveCandidates.extend(self.rook.getValidMoves())
        
        #Positive Slope, Negative Slope, Up Down, Left Right
        return moveCandidates

    def makeMove(self, square):
        current = self.getCurrentSquare()
        self.setCurrentSquare(square)
        current.reset()