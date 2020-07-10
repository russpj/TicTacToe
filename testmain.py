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
from TicTacToe import ScoreBoard
from TicTacToe import MoveValidation

from game import StringFromBoard


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


def TestScoreBoard(verbose):
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
		score = ScoreBoard(board)
		passed = (catsGame == expected)
		if verbose or not passed:
			print()
			print('TestIsCatsGame')
			print(StringFromBoard(board))
			print ('  result was \n{}, \nexpected \n{}'.format(score, expected))

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


tests = (TestCondition(TestIsWinner, False),
				 TestCondition(TestValidateMove, False),
				 TestCondition(TestMove, False),
				 TestCondition(TestIsCatsGame, False),
				 TestCondition(TestScoreBoard, True)
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

