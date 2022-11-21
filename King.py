from Piece import Piece

class King(Piece):

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        self.name = "King"
