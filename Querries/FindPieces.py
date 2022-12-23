import mysql.connector

class FindPieces:
    conn = None
    cursor = None

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


    def selectAll(self):
        FindPieces.cursor.execute(
            "Select * \
            From location as L\
            Where L.GameID = 1"
        )
        return FindPieces.cursor.fetchall()

    def select_row(self, row):
        FindPieces.cursor.execute(
            "Select * \
            From location as L\
            Where L.Row = " + str(row) + 
            " AND L.GameID = 1 \
            Order By L.Row ASC"
        )
        return FindPieces.cursor.fetchall()
    
    def select_col(self, col):
        FindPieces.cursor.execute(
            "Select * \
            From location as L\
            Where L.Col = " + str(col) + 
            " AND L.GameID = 1 \
            Order By L.Col ASC"
        )
        return FindPieces.cursor.fetchall()





if __name__ == '__main__':
    tst = FindPieces()
    for x in tst.selectAll():
        print(x)