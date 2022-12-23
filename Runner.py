from Board import Board
from Pieces.Piece import Piece
from Pieces.PieceColor import PieceColor
from Pieces.Rook import Rook
from Pieces.Queen import Queen
from Querries.FindPieces import FindPieces

def main():
    db = FindPieces()
    db_res = None
    #board = Board()
    # board.printBoard()
    color = PieceColor("Dark")

    db_res = db.selectAll()
    rook = Rook(color)
    rook.setCurrentSquare((0,0))

    print(rook.getValidMoves())
    

    

if __name__ == '__main__':
    main()