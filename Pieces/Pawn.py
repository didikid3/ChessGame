from Pieces.Piece import Piece
from Board import Board
from Querries.FindPieces import FindPieces


def checkEmpty(item, res, pos):
        if len(item) == 0:
            res[pos] = 1
class Pawn(Piece):

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "Pawn"

    
    def getValidMoves(self):
        db = FindPieces()
        cur_row = self.getCurrentSquare()[0]
        cur_col = self.getCurrentSquare()[1]
        color = self.getPieceColor()

        print(self.getName() + "-> getValidMoves")
        res = [0,0,0]   #Forward, Left Diag, Right Diag
        dis = 1 if color == 'White' else -1
        tmp = db.check_for_piece(cur_row+dis, cur_col)
        
        checkEmpty(tmp, res, 0)
        if cur_col != 0:
            tmp = db.check_for_piece(cur_row+dis, cur_col-1)
            checkEmpty(tmp, res, 1)
        if cur_col != 7:
            tmp = db.check_for_piece(cur_row+dis, cur_col+1)
            checkEmpty(tmp, res, 2)
        
        #Returns boolean values
        #[Can Move Forward, Move Left Diag, Move Right Diag]
        return res

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")