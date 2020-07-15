"""
This handles the game play of Tic-Tac-Toe
"""


from TicTacToe import IsWinner
from TicTacToe import IsCatsGame
from TicTacToe import ValidateMove
from TicTacToe import Move
from TicTacToe import IndexBoard
from TicTacToe import CanonicalizeBoard
from TicTacToe import BoardFromIndex
from TicTacToe import MoveValidation

from matchbox import matchboxes
from matchbox import GetComputerMove


def StringFromBoard(board):
	"""
	Prepares a string representation of the board
	for pretty printing. It is a multi line string.
	"""
	rows = []
	for row in board:
		rows.append('|'.join([' '+square+' ' for square in row]))
	return '\n-----------\n'.join(rows)


def StringFromMatchbox(index):
	"""
	Takes the index, computes the board and the extracts the matchbox
	and makes a pretty picture out of them
	"""
	board = BoardFromIndex(index)
	matchbox = matchboxes[index]

	output = []
	for row in range(3):
		squares = []
		for col in range(3):
			if board[row][col] == ' ':
				squares.append('{:^3}'.format(matchbox[row*3 + col]))
			else:
				squares.append('{:^3}'.format(board[row][col]))
		output.append('|'.join(squares))
	return '\n-----------\n'.join(output)



def GetNextMove(board, index, teams, mover):
	"""
	Prompts the appropriate user for their next move.
	Won't leave until a valid input is entered, or an excpetion
	is thrown (if a non-numeric input is entered)
	"""
	if teams[mover] == 'H':
		while True:
			move = int(input('Tell me your move, {}: '.format(mover)))
			result = ValidateMove(board, mover, move)
			if result == MoveValidation.Valid:
				return move
	else:
		return GetComputerMove(board, index, mover)


def PlayTicTacToe(numPlayers):
	"""
	Manages the input and output for a Tic Tac Toe game
	Does check for valid moves, and will detect won games and 
	cat's games
	"""
	teams = {} # maps the teams onto players or computer
	if numPlayers == 0:
		teams['X'] = 'C'
		teams['O'] = 'C'
	elif numPlayers == 1:
		teams['X'] = 'H'
		teams['O'] = 'C'
	else:
		teams['X'] = 'H'
		teams['O'] = 'H'

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
		index = IndexBoard(board)
		game.append('I {}'.format(index))
		nextPlayer = teams[nextMover]
		if nextPlayer == 'H':
			move = GetNextMove(board, index, teams, nextMover)
		else:
			move = GetComputerMove(board, index, nextMover)
			print('The Computer has chosen {}.'.format(move))
		Move(board, nextMover, move)
		game.append('M {} {}'.format(nextMover, move))
		print(StringFromBoard(board))

		canonicalBoard, index, rotations, flips = CanonicalizeBoard(board)
		if rotations > 0:
			print('Rotate {} times'.format(rotations))
			game.append('R {}'.format(rotations))
		if flips > 0:
			print ('Flip Horizontally')
			game.append('F {}'.format(flips))
		if rotations > 0 or flips > 0:
			board = canonicalBoard
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
	"""
	Saves the given list

	For TicTacToe, we expect these lines in the list
	I {number}	The index number for the board at the beginning of the move
	M {team} {square}
	R {rotations}	optional number of rotations to canonicalize the board
	F {flips} optional number of horizontal flips to canonicalize the board
	W {team} if the games results in a win for team
	C if the game results in a cat's game
	"""
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
			numPlayers = int(input('How many human players, Professor? '))
			game = PlayTicTacToe(numPlayers)
			ticTacToeGames.append(game)

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