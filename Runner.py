from Board import Board
from Pieces.Piece import Piece
from Pieces.PieceColor import PieceColor
from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.King import King
from Querries.FindPieces import FindPieces
from Board import Board

def main():
    db = FindPieces()

    board = Board()
    querry = db.selectAll()
    board.setBoard(querry)
    for x in board.getBoard():
        if x.getName() == 'Bishop' and x.getCurrentSquare() == (3,3):
            print(x.getCurrentSquare())
            x.getValidMoves()

    

   

def setBoard(board):
    color_black = PieceColor("Dark")
    color_white = PieceColor("White")

    for row in range(1,7,5):
        for col in range(0, 8):
            pawn = Pawn(color_white if row==1 else color_black)
            pawn.setCurrentSquare((row, col))
            board.append(pawn)

    for row in range(0,8,7):
        rook1 = Rook(color_white if row==0 else color_black)
        rook2 = Rook(color_white if row==0 else color_black)

        knight1 = Knight(color_white if row==0 else color_black)
        knight2 = Knight(color_white if row==0 else color_black)

        bishop1 = Bishop(color_white if row==0 else color_black)
        bishop2 = Bishop(color_white if row==0 else color_black)

        king = King(color_white if row==0 else color_black)
        queen = Queen(color_white if row==0 else color_black)

        rook1.setCurrentSquare((row, 0))
        rook2.setCurrentSquare((row, 7))
        knight1.setCurrentSquare((row, 1))
        knight2.setCurrentSquare((row, 6))
        bishop1.setCurrentSquare((row, 2))
        bishop2.setCurrentSquare((row, 5))
        queen.setCurrentSquare((row, 3))
        king.setCurrentSquare((row, 4))

        board.append(rook1)
        board.append(rook2)
        board.append(knight1)
        board.append(knight2)
        board.append(bishop1)
        board.append(bishop2)
        board.append(queen)
        board.append(king)


if __name__ == '__main__':
    main()