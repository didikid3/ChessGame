from Piece import Piece

class Pawn(Piece):

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        self.name = "Pawn"
