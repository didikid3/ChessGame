class PieceColor:
    def __init__(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def __str__(self):
        return self.color