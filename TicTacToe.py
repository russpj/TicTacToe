"""
TicTacToe

Contains the engines for a Tic-Tac-Toe board
"""

from enum import Enum
from copy import deepcopy

def IsWinner(board, team):
	"""
	Input
		board: a double list of the squares on a Tic-Tac-Toe baord
		team: X or O

		returns True iff team has won
	"""
	for row in range(3):
		allTeam = True
		for col in range(3):
			if board[row][col] != team:
				allTeam = False
		if allTeam:
			return True
	
	for col in range(3):
		allTeam = True
		for row in range(3):
			if board[row][col] != team:
				allTeam = False
		if allTeam:
			return True

	allTeam = True
	for index in range(3):
		if board[index][index] != team:
			allTeam = False
	if allTeam:
		return True

	return board[0][2] == team and board[1][1] == team and board[2][0] == team


def Count(board, team):
	"""
	Counts the number of squares already picked by the team in the board
	"""
	count = 0
	for row in board:
		for square in row:
			if square == team:
				count += 1
	return count


def IsCatsGame(board):
	return not IsWinner(board, 'X') and not IsWinner(board, 'O') and Count(board, 'X') == 5


class MoveValidation(Enum):
	Valid = 1
	WrongTeam = 2
	OutOfRange = 3
	Occupied = 4
	NYI = 9

def ValidateMove(board, team, move):
	"""
	Validates that the right team is moving, and that the move is into a valid, empty square
	"""

	numX = Count(board, 'X')
	numO = Count(board, 'O')
	if team == 'X' and numX != numO:
		return MoveValidation.WrongTeam

	if team == 'O' and numX != numO+1:
		return MoveValidation.WrongTeam

	if move < 0 or move >= 9:
		return MoveValidation.OutOfRange

	row = move//3
	col = move%3
	if board[row][col] != ' ':
		return MoveValidation.Occupied

	return MoveValidation.Valid


def Move(board, team, move):
	"""
	Makes the move for the team on the board

	Fills in the square with team's letter
	"""
	row = move//3
	col = move%3
	board[row][col] = team
	return

def IndexBoard(board):
	"""
	Assigns a unique index to the board, using base 3 where blanks are 0, O's are 1, and X's are 2
	"""
	def Value(square):
		return 2 if square=='X' else 1 if square=='O' else 0

	result = 0
	for row in board:
		for square in row:
			result = result*3 + Value(square)
	return result

def RotateBoard(board):
	"""
	Rotates a TicTacToe board clockwise

	0|1|2          6|3|0
	-----					 ----- 
	3|4|5    ==>   7|4|1
	-----          -----
	6|7|8					 8|5|2
	"""
	newBoard = []
	for row in range(3):
		newLine = []
		for col in range(3):
			newLine.append(board[2-col][row])
		newBoard.append(newLine)
	return newBoard

def FlipBoard(board):
	"""
	Flips a TicTacToe board horizontally

	0|1|2          2|1|0
	-----					 ----- 
	3|4|5    ==>   5|4|3
	-----          -----
	6|7|8					 8|7|6
	"""
	newBoard = []
	for row in range(3):
		newLine = []
		for col in range(3):
			newLine.append(board[row][2-col])
		newBoard.append(newLine)
	return newBoard

def EqualBoards(left, right):
	"""
	Determines if all of the squares in the two boards are equal
	"""
	for row in range(3):
		for col in range(3):
			if left[row][col] != right[row][col]:
				return False
	return True


def CanonicalizeBoard(boardParam):
	"""
	Finds the rotation and reversal of the board that yields the
	highest index, and uses that as the standard version of the board

	returns a tuple of (board, index, rotations, flips)
	"""
	indexMax = 0
	flipsOnMax = 0
	rotaionsOnMax = 0
	board = boardParam
	boardReturn = deepcopy(board)
	for flips in range(2):
		for rotations in range(4):
			index = IndexBoard(board)
			if index > indexMax:
				indexMax = index
				flipsOnMax = flips
				rotationsOnMax = rotations
				boardReturn = deepcopy(board)
			board = RotateBoard(board)
		board = FlipBoard(board)
	return (boardReturn, indexMax, rotationsOnMax, flipsOnMax)


def BoardFromIndex(index):
	"""
	Creates a board from its unique index
	"""
	charList = []
	while index > 0:
		nextDigit = index % 3
		nextChar = ' ' if nextDigit == 0 else 'O' if nextDigit == 1 else 'X'
		charList.append(nextChar)
		index = index // 3

	while len(charList) < 9:
		charList.append(' ')

	charListDescending = charList[::-1]

	board = []
	for row in range(3):
		board.append(charListDescending[row*3:(row+1)*3])

	return board