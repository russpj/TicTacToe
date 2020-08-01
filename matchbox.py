"""
matchbox.py

Implements a matchbox style machine learning bed for TicTacToe
"""

from itertools import accumulate
from random import choices
from random import seed
from TicTacToe import BoardFromIndex


matchboxes = {}
seed()

def DefaultMatchbox(index):
	"""
	Creates a default matchbox for this index

	The default will have 0.0 probability for every occupied square,
	and 1.0 probability for every empty square
	"""
	board = BoardFromIndex(index)
	matchbox = []
	for row in range(3):
		for col in range(3):
			matchbox.append(5 if board[row][col] == ' ' else 0)
	return matchbox

def PickSquareAtRandom(matchbox):
	"""
	Picks one of the squares from the matchbox

	The probability of a square being chosen is based on its 
	relative weight in the matchbox
	"""
	squares = range(9)
	square = choices(squares, weights=matchbox)
	return square[0]


def GetComputerMove(board, index, mover):
	"""
	Uses the matchbox to get a decent random move

	First looks up the index in matchboxes. If it is there, 
	returns the value. Otherwise it returns a new, default matchbox.
	"""
	if index in matchboxes:
		matchbox = matchboxes[index]
	else:
		matchbox = DefaultMatchbox(index)
		matchboxes[index] = matchbox
	return PickSquareAtRandom(matchbox)


def LearnFromGames(game):
	"""
	Takes a list of strings for the game, and updates the matchboxes
	for the moves that the winner or loser took. No change if the game
	was a cat's game.
	"""
	parsedGames = ParseGames(game)
	for parsedGame in parsedGames:
		if parsedGame.winner != 'C':
			winner = parsedGame.winner
			for move in parsedGame.moves:
				if move.index in matchboxes:
					matchbox = matchboxes[move.index]
				else:
					matchbox = DefaultMatchbox(move.index)
				if sum(matchbox) == 1:
					# There is only one bead left in the matchbox. Don't remove it!
					break
				weightIncrement = 1 if move.mover == winner else -1
				matchbox[move.square] += weightIncrement
				matchboxes[move.index] = matchbox
	return


def ClearMatchboxes():
	global matchboxes
	matchboxes = {}
	return


def GetMatchboxes():
	return matchboxes


class ParsedMove:
	"""
	A single move of a game, with it's board index, the mover, and the chosen square
	"""
	def __init__(self, index, mover, square):
		self.index = index
		self.mover = mover
		self.square = square
		return

	def __str__(self):
		return f'Index: {self.index}, Team: {self.mover}, Square: {self.square}'

class ParsedGame:
	"""
	A full game, with the winner, and the list of moves
	"""
	def __init__(self):
		self.winner = ' '
		self.moves = []
		return

	def __str__(self):
		output = self.winner
		for move in self.moves:
			output += '\n' + str(move)
		return output

def ParseGames(gameList):
	"""
	Parses the game.
	Assumes that the last line begins with 'C' or 'W'
	Then a move is an 'I' line followed by a 'M' line
	Board transformation lines are ignored
	"""
	games = []
	game = ParsedGame()
	for line in gameList:
		tokens = line.split(' ')
		if tokens[0] == 'I':
			index = int(tokens[1])
		elif tokens[0] == 'M':
			mover, square = tokens[1:]
			game.moves.append(ParsedMove(index, mover, int(square)))
		elif tokens[0] == 'C':
			game.winner = 'C'
			games.append(game)
			game = ParsedGame()
		elif tokens[0] == 'W':
			game.winner = tokens[1]
			games.append(game)
			game = ParsedGame()
	return games


