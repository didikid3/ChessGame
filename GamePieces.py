class Piece:
	def __init__ (self, type, team, eatable=False):
		self.type = type
		self.team = team
		self.eatable = eatable

	def loadPicture(self):
		if self.team == 0:
			self.sprite = 'white_'
		else:
			self.sprite = 'black_'
			
		if self.type == 'pawn':
			self.sprite += 'pawn.png'
		elif self.type == 'rook':
			self.sprite += 'rook.png'
		elif self.type == 'bishop':
			self.sprite += 'bishop.png'
		elif self.type == 'knight':
			self.sprite += 'knight.png'
		elif self.type == 'queen':
			self.sprite += 'queen.png'
		elif self.type == 'king':
			self.sprite += 'king.png'