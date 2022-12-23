import Pieces
class Board:
    def __init__(self):
        self.board = []

    def getBoard(self):
        return self.board
        
    def setBoard(self, board):
        for item in board:
            if item[2] == 'Pawn':
                piece = Pieces.Pawn.Pawn(item[1])
            elif item[2] == 'Rook':
                piece = Pieces.Rook.Rook(item[1])
            elif item[2] == 'Knight':
                piece = Pieces.Knight.Knight(item[1])
            elif item[2] == 'Bishop':
                piece = Pieces.Bishop.Bishop(item[1])
            elif item[2] == 'Queen':
                piece = Pieces.Queen.Queen(item[1])
            elif item[2] == 'King':
                piece = Pieces.King.King(item[1])

            piece.setCurrentSquare((item[3], item[4]))
            self.board.append(piece)