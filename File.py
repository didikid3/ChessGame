class File:

    def __init__(self, file):
        self.file = file
    
    def getFile(self):
        return self.file
    def setFile(self, file):
        self.file = file

    def __str__(self):
        return self.file