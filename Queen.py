from Piece import Piece

class Queen(Piece):

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        self.name = "Queen"
