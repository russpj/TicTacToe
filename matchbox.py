"""
matchbox.py

Implements a matchbox style machine learning bed for TicTacToe
"""

from itertools import accumulate
from random import choices
from TicTacToe import BoardFromIndex


matchboxes = {}

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

def LearnFromGame(game):
	"""
	Takes a list of strings for the game, and updates the matchboxes
	for the moves that the winner or loser took. No change if the game
	was a cat's game.
	"""
	return
