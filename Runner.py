from Board import Board
from Pieces.Piece import Piece
from Pieces.PieceColor import PieceColor
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
def main():
    # board = Board()
    # board.printBoard()
    color = PieceColor("Dark")

    pawn = Pawn(color)
    pawn.getValidMoves(None)

    

main()