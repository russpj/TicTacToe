"""
Runs some tests.

Some tests will assert only if they fail
Other tests show how the algorithms are working
"""

from TicTacToe import IsWinner
from TicTacToe import ValidateMove
from TicTacToe import MoveValidation

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
			print(board)
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
			print(board)
			print('  testing with {} in {}'.format(team, move))
			print ('  result was {}, expected {}'.format(result, expected))

		if result != expected:
			print ('FAILED')
			return False
		else:
			return True
		return False

	allTestsPassed = True
	allTestsPassed = TestAssert(xMove, 'O', 5, MoveValidation.WrongTeam, verbose)
	allTestsPassed = TestAssert(xMove, 'X', 10, MoveValidation.OutOfRange, verbose)
	return allTestsPassed


tests = (TestCondition(TestIsWinner, False),
				 TestCondition(TestValidateMove, False)
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

