import sys
global N

def is_safe(board, row, col):
	for i in range(col):
		if board[row][i] == 1:
			return False
	for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	for i,j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	return True

def solve_NQ_util(board, col):
	if col >= N:
		return True
	
	# row
	for i in range(N):
		if is_safe(board, i, col):
			board[i][col] = 1
			if solve_NQ_util(board, col + 1) == True:
				return True
			board[i][col] = 0
	return False

def n_queen():
	board = [[0 for i in range(N)] for i in range(N)]
	if solve_NQ_util(board, 0) == True:
		print board

##################################################
#				    	main					 #
##################################################

N=int(sys.argv[1])
n_queen()
