from GamePieces import Piece

board = [['' for i in range(8)] for i in range(8)]


def createBoard(gameBoard):
	board[0] = [Piece('rook', 1), Piece('knight', 1), 
				Piece('bishop', 1), Piece('queen', 1), 
				Piece('king', 1), Piece('bishop', 1), 
                Piece('knight', 1), Piece('rook', 1)
                ]

	board[7] = [Piece('rook', 0), Piece('knight', 0), 
				Piece('bishop', 0), Piece('queen', 0), 
				Piece('king', 0), Piece('bishop', 0), 
	            Piece('knight', 0), Piece('rook', 0)
	            ]

	for i in range(8):
	    board[1][i] = Piece('pawn', 1, 'b_pawn.png')
	    board[6][i] = Piece('pawn', 0, 'w_pawn.png')
	return board

board = createBoard(board)
print(board)