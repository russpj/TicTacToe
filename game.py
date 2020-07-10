"""
This handles the game play of Tic-Tac-Toe
"""


from TicTacToe import IsWinner
from TicTacToe import IsCatsGame
from TicTacToe import ValidateMove
from TicTacToe import Move
from TicTacToe import MoveValidation


def StringFromBoard(board):
	"""
	Prepares a string representation of the board
	for pretty printing. It is a multi line string.
	"""
	rows = []
	for row in board:
		rows.append('|'.join(row))
	return '\n-----\n'.join(rows)


def GetNextMove(board, mover):
	"""
	Prompts the appropriate user for their next move.
	Won't leave until a valid input is entered, or an excpetion
	is thrown (if a non-numeric input is entered)
	"""
	while True:
		move = int(input('Tell me your move, {}: '.format(mover)))
		result = ValidateMove(board, mover, move)
		if result == MoveValidation.Valid:
			return move


def PlayTicTacToe(numPlayers):
	"""
	Manages the input and output for a Tic Tac Toe game
	numPlayers is currently assumed to be 2
	Does check for valid moves, and will detect won games and 
	cat's games
	"""
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
	game = []
	while True:
		move = GetNextMove(board, nextMover)
		Move(board, nextMover, move)
		game.append('M {} {}'.format(nextMover, move))
		print(StringFromBoard(board))
		
		if IsWinner(board, nextMover):
			print ('{} is the Winner!'.format(nextMover))
			game.append('W {}'.format(nextMover))
			break
		
		if IsCatsGame(board):
			print("No winner! Cat's game.")
			game.append('C')
			break

		if nextMover == 'X':
			nextMover = 'O'
		else:
			nextMover = 'X'
	return game

def SaveListInFile(games):
	while True:
		fileName = input('What file should we write to, Professor? ')
		try:
			with open(fileName, 'a') as file:
				for game in games:
					for move in game:
						file.write(move + '\n')
			break
		except OSError as error:
			print('{}, try again.'.format(error))
	return

def Play():
	"""
	Gets the user started on a game. Note that the only game currently
	available is TicTacToe.

	ToDo: implement Global Thermonuclear War
	"""
	ticTacToeGames = []
	while True:
		gameName = input('Would you like to play a game, Professor? ')
		if gameName == 'TicTacToe':
			ticTacToeGames.append(PlayTicTacToe(2))
		elif gameName == 'Save':
			SaveListInFile(ticTacToeGames)
		elif gameName == "No":
			print ('Good-Bye, Professor')
			break
		else:
			print("I don't know how to play {}".format(gameName))
	return

if __name__ == '__main__':
	"""
	If this module is the main module, then Play a game.
	"""
	Play()