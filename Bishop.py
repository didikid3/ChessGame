from Piece import Piece

class Bishop(Piece):

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        self.name = "Bishop"