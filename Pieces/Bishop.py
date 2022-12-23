from Pieces.Piece import Piece
from Board import Board
from Querries.FindPieces import FindPieces


class Bishop(Piece):
    

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "Bishop"

    def getValidMoves(self):
        db = FindPieces()

        cur_row = self.getCurrentSquare()[0]
        cur_col = self.getCurrentSquare()[1]

        diag = db.select_diag(cur_row, cur_col)
        return diag



    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")
