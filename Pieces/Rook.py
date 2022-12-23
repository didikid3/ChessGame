from Pieces.Piece import Piece
from Board import Board
from Querries.FindPieces import FindPieces

class Rook(Piece):

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "Rook"

    def getValidMoves(self):
        db = FindPieces()

        range_row = [0,7]
        range_col = [0,7]
        cur_row = self.getCurrentSquare()[0]
        cur_col = self.getCurrentSquare()[1]

        row_data = db.select_row(cur_row)
        col_data = db.select_col(cur_col)

        for piece in row_data:
            col = int(piece[4])
            if col < cur_col:
                range_col[0] = col
            elif col > cur_col:
                range_col[1] = col
                break
        for piece in col_data:
            row = int(piece[3])
            if row < cur_row:
                range_row[0] = row
            elif row > cur_row:
                range_row[1] = row
                break

        '''
        print("Same Col, Different Rows:")
        print(range_row)
        print("Same Row, Different Cols:")
        print(range_col)
        '''

        return range_row, range_col
        
        

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")