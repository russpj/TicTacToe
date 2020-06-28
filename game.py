"""
This handles the game play of Tic-Tac-Toe
"""


from TicTacToe import IsWinner
from TicTacToe import ValidateMove
from TicTacToe import Move
from TicTacToe import MoveValidation


def StringFromBoard(board):
	rows = []
	for row in board:
		rows.append('|'.join(row))
	return '\n-----\n'.join(rows)


def Play():
	gameName = input('Would you like to play a game, Professor? ')
	if gameName == 'TicTacToe':
		numberBoard = [
				['0', '1', '2'],
				['3', '4', '5'],
				['6', '7', '8']
			]
		print('Thank you. The board is numbered like this:')
		print(StringFromBoard(numberBoard))
	else:
		print("I don't want to play {}".format(gameName))
	return

if __name__ == '__main__':
	Play()