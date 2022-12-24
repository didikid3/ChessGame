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
            if piece[3] == cur_row and piece[4] == cur_col:
                continue

            col = int(piece[4])
            if col < cur_col:
                if piece[1] != self.getPieceColor():
                    range_col[0] = col
                else:
                    range_col[0] = col + 1
            elif col > cur_col:
                if piece[1] != self.getPieceColor():
                    range_col[1] = col
                else:
                    range_col[1] = col - 1

                break

        for piece in col_data:
            if piece[3] == cur_row and piece[4] == cur_col:
                continue

            row = int(piece[3])
            if row < cur_row:
                if piece[1] != self.getPieceColor():
                    range_row[0] = row
                else:
                    range_row[0] = row + 1

            elif row > cur_row:
                if piece[1] != self.getPieceColor():
                    range_row[1] = row
                else:
                    range_row[1] = row - 1
                break

        '''
        #UP DOWN
        print(range_row)
        #LEFT RIGHT
        print(range_col)
        '''

        return range_row, range_col
        
        

    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")