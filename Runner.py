from Board import Board
from Piece import Piece
from PieceColor import PieceColor
from Pawn import Pawn
from Queen import Queen
def main():
    # board = Board()
    # board.printBoard()
    color = PieceColor("Dark")

    pawn = Pawn(color)
    queen = Queen(color)
    print(pawn)
    print(queen)

    

main()