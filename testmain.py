"""
Runs some tests.

Some tests will assert only if they fail
Other tests show how the algorithms are working
"""

from copy import deepcopy

from TicTacToe import IsWinner
from TicTacToe import IsCatsGame
from TicTacToe import ValidateMove
from TicTacToe import Move
from TicTacToe import Count
from TicTacToe import IndexBoard
from TicTacToe import RotateBoard
from TicTacToe import FlipBoard
from TicTacToe import EqualBoards
from TicTacToe import CanonicalizeBoard
from TicTacToe import BoardFromIndex
from TicTacToe import MoveValidation

from matchbox import matchboxes
from matchbox import DefaultMatchbox
from matchbox import PickSquareAtRandom
from matchbox import GetComputerMove

from game import StringFromBoard
from game import StringFromMatchbox


class TestCondition:
	"""
	Simple struct to encapsulate a test that should be run

	runTest is the function to run
	verbose is True if the function should print out results as well as 
		return false
	"""
	def __init__(self, runTest, verbose):
			self.runTest = runTest
			self.verbose = verbose

def TestIsWinner(verbose):
	"""
	Tests the IsWinner function

	verbose should be True to trigger printing results

	Tests no winner, x as winner, o as winner, column winners, row winners and both
		diagonals
	"""
	noWinner = [
			['X', 'O', ' '],
			['O', 'O', ' '],
			['X', 'X', ' '],
		]
	xWinner = [
			['X', 'O', ' '],
			['X', 'O', ' '],
			['X', 'X', ' '],
		]
	oWinner = [
			['X', 'X', 'O'],
			['O', 'O', 'X'],
			['O', 'X', 'X'],
		]
	bothWinner = [
			['X', 'O', ' '],
			['O', 'O', 'O'],
			['X', 'X', 'X'],
		]
	diagWinner = [
			['X', 'O', ' '],
			['O', 'X', 'O'],
			['X', 'O', 'X'],
		]

	def TestAssert(board, team, expected, verbose):
		result = IsWinner(board, team)
		if verbose or result!=expected:
			print()
			print('TestIsWinner')
			print(StringFromBoard(board))
			print('  testing with {}'.format(team))
			print ('  result was {}'.format(result))

		if result != expected:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	allTestsPassed = TestAssert(noWinner, 'X', False, verbose) and allTestsPassed
	allTestsPassed = TestAssert(noWinner, 'O', False, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xWinner, 'X', True, verbose) and allTestsPassed
	allTestsPassed = TestAssert(oWinner, 'O', True, verbose) and allTestsPassed
	allTestsPassed = TestAssert(bothWinner, 'X', True, verbose) and allTestsPassed
	allTestsPassed = TestAssert(bothWinner, 'O', True, verbose) and allTestsPassed
	allTestsPassed = TestAssert(diagWinner, 'X', True, verbose) and allTestsPassed
	return allTestsPassed


def TestValidateMove(verbose):
	"""
	Tests the ValidateMove function, with wrong turns, out of bounds moves
	"""
	xMove = [
			['X', ' ', 'O'],
			[' ', 'X', ' '],
			[' ', ' ', 'O']
		]
	yMove = [
			['X', ' ', 'O'],
			[' ', 'X', ' '],
			[' ', ' ', ' ']
		]

	def TestAssert(board, team, move, expected, verbose):
		result = ValidateMove(board, team, move)
		if verbose or result!=expected:
			print()
			print('TestValidateMove')
			print(StringFromBoard(board))
			print('  testing with {} in {}'.format(team, move))
			print ('  result was {}, expected {}'.format(result, expected))

		if result != expected:
			print ('FAILED')
			return False
		else:
			return True
		return False

	allTestsPassed = True
	allTestsPassed = TestAssert(xMove, 'O', 5, MoveValidation.WrongTeam, verbose) and allTestsPassed
	allTestsPassed = TestAssert(yMove, 'X', 8, MoveValidation.WrongTeam, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xMove, 'X', 10, MoveValidation.OutOfRange, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xMove, 'X', -1, MoveValidation.OutOfRange, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xMove, 'X', 2, MoveValidation.Occupied, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xMove, 'X', 4, MoveValidation.Occupied, verbose) and allTestsPassed
	allTestsPassed = TestAssert(yMove, 'Y', 4, MoveValidation.Occupied, verbose) and allTestsPassed
	allTestsPassed = TestAssert(yMove, 'Y', 2, MoveValidation.Occupied, verbose) and allTestsPassed
	allTestsPassed = TestAssert(yMove, 'Y', 8, MoveValidation.Valid, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xMove, 'X', 5, MoveValidation.Valid, verbose) and allTestsPassed
	return allTestsPassed


def TestMove(verbose):
	xMove = [
			['X', ' ', 'O'],
			[' ', 'X', ' '],
			[' ', ' ', 'O']
		]
	xMoveExpected = [
			['X', ' ', 'O'],
			[' ', 'X', 'X'],
			[' ', ' ', 'O']
		]
	yMove = [
			['X', ' ', 'O'],
			[' ', 'X', ' '],
			[' ', ' ', ' ']
		]
	yMoveExpected = [
			['X', ' ', 'O'],
			[' ', 'X', ' '],
			[' ', ' ', 'O']
		]
	
	def TestAssert(board, team, move, expected, verbose):
		newBoard = deepcopy(board)
		Move(newBoard, team, move)
		result = (newBoard == expected)
		if verbose or not result:
			print()
			print('TestMove')
			print(StringFromBoard(board))
			print('  testing with {} in {}'.format(team, move))
			print ('  result was \n{}, \nexpected \n{}'.format(StringFromBoard(board), StringFromBoard(expected)))

		if not result:
			print ('FAILED')
			return False
		else:
			return True
		return False

	allTestsPassed = True
	allTestsPassed = TestAssert(xMove, 'X', 5, xMoveExpected, verbose) and allTestsPassed
	allTestsPassed = TestAssert(yMove, 'O', 8, yMoveExpected, verbose) and allTestsPassed
	return allTestsPassed


def TestIsCatsGame(verbose):
	notFull = (
			('X', ' ', 'O'),
			('O', 'X', 'X'),
			(' ', ' ', 'O')
		)
	xWinner = [
			['X', 'O', 'O'],
			['X', 'O', 'X'],
			['X', 'X', 'O'],
		]
	oWinner = [
			['X', 'X', 'O'],
			['O', 'O', 'X'],
			['O', 'X', 'X'],
		]
	catsGame = [
			['X', 'X', 'O'],
			['O', 'O', 'X'],
			['X', 'O', 'X'],
		]

	def TestAssert(board, expected, verbose):
		catsGame = IsCatsGame(board)
		passed = (catsGame == expected)
		if verbose or not passed:
			print()
			print('TestIsCatsGame')
			print(StringFromBoard(board))
			print ('  result was \n{}, \nexpected \n{}'.format(catsGame, expected))

		if not passed:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	allTestsPassed = TestAssert(notFull, False, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xWinner, False, verbose) and allTestsPassed
	allTestsPassed = TestAssert(oWinner, False, verbose) and allTestsPassed
	allTestsPassed = TestAssert(catsGame, True, verbose) and allTestsPassed
	return allTestsPassed


def TestIndexBoard(verbose):
	notFull = (
			('X', ' ', 'O'),
			('O', 'X', 'X'),
			(' ', ' ', 'O')
		)
	xWinner = [
			['X', 'O', 'O'],
			['X', 'O', 'X'],
			['X', 'X', 'O'],
		]
	oWinner = [
			['X', 'X', 'O'],
			['O', 'O', 'X'],
			['O', 'X', 'X'],
		]
	catsGame = [
			['X', 'X', 'O'],
			['O', 'O', 'X'],
			['X', 'O', 'X'],
		]

	def TestAssert(board, expected, verbose):
		score = IndexBoard(board)
		passed = (score == expected)
		if verbose or not passed:
			print()
			print('TestIsCatsGame')
			print(StringFromBoard(board))
			print ('  result was {}, expected {}'.format(score, expected))

		if not passed:
			print ('FAILED')
			return False
		else:
			return True
		return False

	allTestsPassed = True
	allTestsPassed = TestAssert(notFull, 14311, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xWinner, 16684, verbose) and allTestsPassed
	allTestsPassed = TestAssert(oWinner, 18620, verbose) and allTestsPassed
	allTestsPassed = TestAssert(catsGame, 18626, verbose) and allTestsPassed
	return allTestsPassed

def TestRotate(verbose):
	notFull = (
			('X', ' ', 'O'),
			('O', 'X', 'X'),
			(' ', ' ', 'O')
		)
	xWinner = (
			('X', 'O', 'O'),
			('X', 'O', 'X'),
			('X', 'X', 'O'),
		)
	oWinner = (
			('X', 'X', 'O'),
			('O', 'O', 'X'),
			('O', 'X', 'X'),
		)
	catsGame = (
			('X', 'X', 'O'),
			('O', 'O', 'X'),
			('X', 'O', 'X'),
		)
	rotatedNotFull = (
			(' ','O','X'),
			(' ','X',' '),
			('O','X','O')
		)
	rotatedXWinner = (
			('X','X','X'),
			('X','O','O'),
			('O','X','O')
		)
	rotatedOWinner = (
			('O','O','X'),
			('X','O','X'),
			('X','X','O')
		)
	rotatedCatsGame = (
			('X','O','X'),
			('O','O','X'),
			('X','X','O')
		)

	def TestAssert(board, expected, verbose):
		newBoard = RotateBoard(board)
		passed = EqualBoards(newBoard, expected)
		if verbose or not passed:
			print()
			print('TestRotateBoard')
			print(StringFromBoard(board))
			print ('  result was \n{}, \nexpected \n{}'.format(
					StringFromBoard(newBoard), StringFromBoard(expected)))

		if not passed:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	allTestsPassed = TestAssert(notFull, rotatedNotFull, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xWinner, rotatedXWinner, verbose) and allTestsPassed
	allTestsPassed = TestAssert(oWinner, rotatedOWinner, verbose) and allTestsPassed
	allTestsPassed = TestAssert(catsGame, rotatedCatsGame, verbose) and allTestsPassed
	return allTestsPassed


def TestFlip(verbose):
	notFull = (
			('X', ' ', 'O'),
			('O', 'X', 'X'),
			(' ', ' ', 'O')
		)
	xWinner = (
			('X', 'O', 'O'),
			('X', 'O', 'X'),
			('X', 'X', 'O'),
		)
	oWinner = (
			('X', 'X', 'O'),
			('O', 'O', 'X'),
			('O', 'X', 'X'),
		)
	catsGame = (
			('X', 'X', 'O'),
			('O', 'O', 'X'),
			('X', 'O', 'X'),
		)
	flippedNotFull = (
			('O',' ','X'),
			('X','X','O'),
			('O',' ',' ')
		)
	flippedXWinner = (
			('O','O','X'),
			('X','O','X'),
			('O','X','X')
		)
	flippedOWinner = (
			('O','X','X'),
			('X','O','O'),
			('X','X','O')
		)
	flippedCatsGame = (
			('O','X','X'),
			('X','O','O'),
			('X','O','X')
		)

	def TestAssert(board, expected, verbose):
		newBoard = FlipBoard(board)
		passed = EqualBoards(newBoard, expected)
		if verbose or not passed:
			print()
			print('TestRotateBoard')
			print(StringFromBoard(board))
			print ('  result was \n{}, \nexpected \n{}'.format(
					StringFromBoard(newBoard), StringFromBoard(expected)))

		if not passed:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	allTestsPassed = TestAssert(notFull, flippedNotFull, verbose) and allTestsPassed
	allTestsPassed = TestAssert(xWinner, flippedXWinner, verbose) and allTestsPassed
	allTestsPassed = TestAssert(oWinner, flippedOWinner, verbose) and allTestsPassed
	allTestsPassed = TestAssert(catsGame, flippedCatsGame, verbose) and allTestsPassed
	return allTestsPassed


def TestCanonicalize(verbose):
	tests = (
			(
				(' ', ' ', ' '),
				(' ', ' ', 'O'),
				(' ', ' ', 'X')
			),
			(
				(' ', ' ', ' '),
				(' ', 'X', 'O'),
				(' ', ' ', ' ')
			),
			(
				(' ', 'O', 'X'),
				(' ', 'X', ' '),
				(' ', ' ', ' ')
			),
		)
	expecteds = (
			(
				(
					('X', 'O', ' '),
					(' ', ' ', ' '),
					(' ', ' ', ' ')
				), 15309, 1, 1
			),
			(
				(
					(' ', 'O', ' '),
					(' ', 'X', ' '),
					(' ', ' ', ' ')
				), 2349, 3, 0
			),
			(
				(
					('X', 'O', ' '),
					(' ', 'X', ' '),
					(' ', ' ', ' ')
				), 15471, 0, 1
			),
		)

	def TestAssert(board, expected, verbose):
		newBoard, index, rotations, flips = CanonicalizeBoard(board)
		passed = EqualBoards(newBoard, expected[0]) 
		passed = passed and index == expected[1] and rotations == expected[2] and flips == expected[3] 
		if verbose or not passed:
			print()
			print('TestCanonicalizeBoard')
			print(StringFromBoard(board))
			print ('  result was \n{}, \nIndex: {}, Rotations: {}, Flips: {}\n'.
							format(StringFromBoard(newBoard), index, rotations, flips) + 
						 '  expected \n{}\nIndex: {}, Rotations: {}, Flips: {}'.
							format(StringFromBoard(expected[0]), expected[1], expected[2], expected[3]))

		if not passed:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	for test, expected in zip(tests, expecteds):
		allTestsPassed = TestAssert(test, expected, verbose) and allTestsPassed

	return allTestsPassed


def TestBoardFromIndex(verbose):
	tests = (
			(
				(' ', ' ', ' '),
				(' ', ' ', 'O'),
				(' ', ' ', 'X')
			),
			(
				(' ', ' ', ' '),
				(' ', 'X', 'O'),
				(' ', ' ', ' ')
			),
			(
				(' ', 'O', 'X'),
				(' ', 'X', ' '),
				(' ', ' ', ' ')
			),
		)

	def TestAssert(board, verbose):
		index = IndexBoard(board)
		newBoard = BoardFromIndex(index)
		passed = EqualBoards(board, newBoard) 
		if verbose or not passed:
			print()
			print('TestBoardFromIndex')
			print(StringFromBoard(board))
			print ('  result was \n{}\n'.
							format(StringFromBoard(newBoard)) + 
						 '  expected \n{}\n'.
							format(StringFromBoard(board)))

		if not passed:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	for test in tests:
		allTestsPassed = TestAssert(test, verbose) and allTestsPassed

	return allTestsPassed


def TestDefaultMatchbox(verbose):
	tests = (
			(
				(' ', ' ', ' '),
				(' ', ' ', 'O'),
				(' ', ' ', 'X')
			),
			(
				(' ', ' ', ' '),
				(' ', 'X', 'O'),
				(' ', ' ', ' ')
			),
			(
				(' ', 'O', 'X'),
				(' ', 'X', ' '),
				(' ', ' ', ' ')
			),
		)
	expecteds = (
			[5, 5, 5, 5, 5, 0, 5, 5, 0],
			[5, 5, 5, 5, 0, 0, 5, 5, 5],
			[5, 0, 0, 5, 0, 5, 5, 5, 5],
		)

	def TestAssert(board, expected, verbose):
		index = IndexBoard(board)
		matchbox = DefaultMatchbox(index)
		passed = matchbox == expected 
		if verbose or not passed:
			print()
			print('TestDefaultMatchbox')
			print(StringFromBoard(board))
			print ('  result was \n{}\n'.
							format((matchbox)) + 
						 '  expected \n{}\n'.
							format((expected)))

		if not passed:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	for test, expected in zip(tests, expecteds):
		allTestsPassed = TestAssert(test, expected, verbose) and allTestsPassed

	return allTestsPassed


def TestPickSquareAtRandom(verbose):
	tests = (
			[5, 5, 5, 5, 5, 0, 5, 5, 0],
			[5, 5, 5, 5, 0, 0, 5, 5, 5],
			[5, 0, 0, 5, 0, 5, 5, 5, 5],
		)

	def TestAssert(matchbox, repetitions, verbose):
		passedAll = True
		for _ in range(repetitions):
			square = PickSquareAtRandom(matchbox)
			passed = matchbox[square] == 5
			if verbose or not passed:
				print('Matchbox, Square, Value = ({} {}, {})'.format(matchbox, square, matchbox[square]))
			passedAll = passedAll and passed

		if not passedAll:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	for test in tests:
		allTestsPassed = TestAssert(test, 10, verbose) and allTestsPassed

	return allTestsPassed


def TestGetComputerMove(verbose):
	tests = (
			(
				(' ', ' ', ' '),
				(' ', ' ', 'O'),
				(' ', ' ', 'X')
			),
			(
				(' ', ' ', ' '),
				(' ', 'X', 'O'),
				(' ', ' ', ' ')
			),
			(
				(' ', 'O', 'X'),
				(' ', 'X', ' '),
				(' ', ' ', ' ')
			),
		)

	def TestAssert(board, index, mover, repetitions, verbose):
		passedAll = True
		for _ in range(repetitions):
			square = GetComputerMove(board, index, mover)
			matchbox = matchboxes[index]
			row = square // 3
			col = square % 3
			passed = board[row][col] == ' ' and matchbox[square] >= 1.0
			if verbose or not passed:
				print()
				print(StringFromBoard(board))
				print('Row: {}, Col {}, Actual: |{}|, Probability: {}'.
					format(row, col, board[row][col], matchbox[square]))
				matchbox[square] += 0.1
				matchboxes[index] = matchbox
			passedAll = passedAll and passed
			print(StringFromMatchbox(index))

		if not passedAll:
			print ('FAILED')
			return False
		else:
			return True

	allTestsPassed = True
	for test in tests:
		mover = 'X' if Count(test, 'X') == Count(test, 'O') else 'O'
		allTestsPassed = TestAssert(test, IndexBoard(test), mover, 10, verbose) and allTestsPassed

	return allTestsPassed


tests = (TestCondition(TestIsWinner, False),
				 TestCondition(TestValidateMove, False),
				 TestCondition(TestMove, False),
				 TestCondition(TestIsCatsGame, False),
				 TestCondition(TestIndexBoard, False),
				 TestCondition(TestRotate, False),
				 TestCondition(TestFlip, False),
				 TestCondition(TestCanonicalize, False),
				 TestCondition(TestBoardFromIndex, False),
				 TestCondition(TestDefaultMatchbox, False),
				 TestCondition(TestPickSquareAtRandom, False),
				 TestCondition(TestGetComputerMove, True)
				 )

def Test():
	numTests = 0
	numFailed = 0
	for test in tests:
		numTests += 1
		if not test.verbose:
			print('.', end='')
		if not test.runTest(test.verbose):
			numFailed += 1
			print("Test Failed")
	print()
	print('{} out of  {} tests succeeded'.format(numTests-numFailed, numTests))

if __name__ == '__main__':
	Test()

