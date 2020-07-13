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
			matchbox.append(1.0 if board[row][col] == ' ' else 0.0)
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

