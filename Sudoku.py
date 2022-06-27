def find_next_empty(puzzle):
	# empty cell in puzzle represent by -1.

	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == -1:
				return r,c

	# if all the cells are filled then return None, None
	return None, None

def is_valid_guess(puzzle, guess, row, col):
	# Given a puzzle , guess , row and col of empty cell. we will check whether the guess is 
	# appropriate at the cell or not as per rules of sudoku.

	# checking row
	row_vals = puzzle[row]
	if guess in row_vals:
		return False

	# checking col
	col_vals = []
	for i in range(9):
		col_vals.append(puzzle[i][col])
	if guess in col_vals:
		return False

	# chekcing 3*3 cubes
	row_start = (row//3)*3
	col_start = (col//3)*3

	cube_vals = []
	for i in range(row_start, row_start+3):
		for j in range(col_start, col_start+3):
			cube_vals.append(puzzle[i][j])
	if guess in cube_vals:
		return False

	return True



def sudoku_solver(puzzle):
	# input puzzle is a list of list , each inner list contains values of one row in our 
	# soduku puzzle.
	# Blank spaces in puzzle is replaced by -1.

	# step 1: find the row, col index of next empty cell in puzzle.
	row, col = find_next_empty(puzzle)

	if row is None:
		return True

	# step 2: guess a number between 1 to 9 to fill in the empty cell.

	for guess in range(1,10):
		
		# step 3 : Check whether the guess is valid or not.
		if is_valid_guess(puzzle, guess, row, col):
			puzzle[row][col] = guess
			if sudoku_solver(puzzle):
				return True
		puzzle[row][col] = -1

	return False


if __name__ == "__main__":

	example_board = [
	[3, 9, -1,   -1, 5, -1,   -1, -1, -1],
	[-1, -1, -1,   2, -1, -1,   -1, -1, 5],
    [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

    [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
    [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

    [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [6, 7, -1,   1, -1, 5,   -1, 4, -1],
    [1, -1, 9,   -1, -1, -1,   2, -1, -1]
	]

	#print(puzzle)
	print(sudoku_solver(example_board))
	print(example_board)

