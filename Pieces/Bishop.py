from Pieces.Piece import Piece
from Board import Board
from Querries.FindPieces import FindPieces


class Bishop(Piece):
    

    def __init__(self, pieceColor):
        Piece.__init__(self, pieceColor)
        self.name = "Bishop"

    def getValidMoves(self):
        print(self.getName() + "-> getValidMoves")
        db = FindPieces()

        #Represents the slope of the diag
        #Range of travel along a row
        positive = [0,7]
        negative = [0,7]
        cur_row = self.getCurrentSquare()[0]
        cur_col = self.getCurrentSquare()[1]

        diag = db.select_diag(cur_row, cur_col)
        for item in diag:
            if item[3] == cur_row and item[4] == cur_col:
                continue

            slope = (item[4] - cur_col) / (item[3] - cur_row)

            if slope > 0:
                if item[3] < cur_row:
                    positive[0] = max(positive[0], item[3])

                    if item[1] == self.getPieceColor() and \
                                    positive[0] == item[3]:
                        positive[0] += 1
                        

                elif item[3] > cur_row:
                    positive[1] = min(positive[1], item[3])

                    if item[1] == self.getPieceColor() and \
                                    positive[1] == item[3]:
                        positive[1] -= 1

            else:
                if item[3] > cur_row:
                    negative[1] = min(negative[1], item[3])

                    if item[1] == self.getPieceColor() and \
                                    negative[1] == item[3]:
                        negative[1] -= 1
                
                elif item[3] < cur_row:
                    negative[0] = max(negative[0], item[3])

                    if item[1] == self.getPieceColor() and \
                                    negative[0] == item[3]:
                        negative[0] += 1     
 

        #Positive slope, negative slope
        #Shows the range of rows possible
        return (positive, negative)



    def makeMove(self, square):
        print(self.getName() + "-> makeMove()")
