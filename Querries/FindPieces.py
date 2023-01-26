import mysql.connector

from Pieces.Piece import Piece


class FindPieces:
    conn = None
    cursor = None
    gameID = "1"

    def __init__(self):
        if FindPieces.conn is None:
            FindPieces.establish_connection()


    def establish_connection():
        FindPieces.conn = mysql.connector.connect(
                host='localhost',
                password='root',
                user='root',
                database='chess')

        if FindPieces.conn.is_connected():
            FindPieces.cursor = FindPieces.conn.cursor()

    def truncateTable(self):
        FindPieces.cursor.execute(
        "TRUNCATE TABLE location"
        )
    
    def newGame(self, pieces):
        for item in pieces:
            FindPieces.cursor.execute(
                "INSERT INTO location \
                 VALUES(" + FindPieces.gameID +
                 ", '" + item.getPieceColor().getColor() +
                 "', '" + item.getName() +
                 "', " + str(item.getCurrentSquare()[0]) +
                 ", " + str(item.getCurrentSquare()[1]) +
                 ")"
            )
        FindPieces.conn.commit()

    def selectAll(self):
        FindPieces.cursor.execute(
            "Select * \
            From location as L\
            Where L.GameID = " + FindPieces.gameID
        )
        return FindPieces.cursor.fetchall()

    def select_row(self, row):
        FindPieces.cursor.execute(
            "Select * \
            From location as L\
            Where L.Row = " + str(row) + 
            " AND L.GameID = " + FindPieces.gameID +
            " Order By L.Row ASC"
        )
        return FindPieces.cursor.fetchall()
    
    def select_col(self, col):
        FindPieces.cursor.execute(
            "Select * \
            From location as L\
            Where L.Col = " + str(col) + 
            " AND L.GameID = " + FindPieces.gameID +
            " Order By L.Col ASC"
        )
        return FindPieces.cursor.fetchall()

    def select_diag(self, row, col):
        
        FindPieces.cursor.execute(
            "Select * \
             From location as L \
             Where L.Row-" + str(row) +
             "= L.Col-" + str(col) +
             " and L.GameID = " + FindPieces.gameID
        )

        res = set(FindPieces.cursor.fetchall())
        FindPieces.cursor.execute(
            "Select * \
             From location as L \
             Where L.Row-" + str(row) +
             "= -1 * (L.Col-" + str(col) +
             ") and L.GameID = " + FindPieces.gameID
        )

        res = res.union(set(FindPieces.cursor.fetchall()))
        return list(res)

    def check_for_piece(self, row, col):
        FindPieces.cursor.execute(
            "Select * \
             From location as L \
             Where L.Row=" + str(row) +
            " and L.Col=" + str(col) +
            " and L.GameID = " + FindPieces.gameID
        )
        return FindPieces.cursor.fetchall()
if __name__ == '__main__':
    tst = FindPieces()
    for x in tst.selectAll():
        print(x)