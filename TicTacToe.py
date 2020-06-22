"""
TicTacToe

Contains the engines for a Tic-Tac-Toe board
"""

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