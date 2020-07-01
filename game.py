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


def GetNextMove(board, mover):
	while True:
		move = int(input('Tell me your move, {}: '.format(mover)))
		result = ValidateMove(board, mover, move)
		if result == MoveValidation.Valid:
			return move


def PlayTicTacToe(numPlayers):
	numberBoard = (
			('0', '1', '2'),
			('3', '4', '5'),
			('6', '7', '8')
		)
	print('Thank you. The board is numbered like this:')
	print(StringFromBoard(numberBoard))
	turn = 'X'
	board = [
			[' ', ' ', ' '],
			[' ', ' ', ' '],
			[' ', ' ', ' ']
		]
	nextMover = 'X'
	while True:
		move = GetNextMove(board, nextMover)
		Move(board, nextMover, move)	
		print(StringFromBoard(board))
		if IsWinner(board, nextMover):
			print ('{} is the Winner!'.format(nextMover))
			break
		if nextMover == 'X':
			nextMover = 'O'
		else:
			nextMover = 'X'

def Play():
	while True:
		gameName = input('Would you like to play a game, Professor? ')
		if gameName == 'TicTacToe':
			PlayTicTacToe(2)
		elif gameName == "No":
			print ('Good-Bye, Professor')
			break
		else:
			print("I don't know how to play {}".format(gameName))
	return

if __name__ == '__main__':
	Play()