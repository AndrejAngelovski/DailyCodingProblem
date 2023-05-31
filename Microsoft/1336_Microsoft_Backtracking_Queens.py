"""
You have an N by N board. Write a function that, given N, returns 
the number of possible arrangements of the board where N queens can
 be placed on the board without threatening each other, i.e. no
two queens share the same row, column, or diagonal.


Theory:

This problem can be solved using backtracking. We can start with 
an empty board and try to place queens in each column one by one,
checking for conflicts with previously placed queens. If a conflict
is detected, we backtrack and try a different row in the same column,
or backtrack further if there are no more rows to try.
"""

def n_queens(n):
    def backtrack(board, col, count):
        if col == n:
            # All queens have been successfully placed on the board
            return count + 1
        else:
            for row in range(n):
                if is_valid(board, row, col):
                    # Place the queen at (row, col)
                    board[row][col] = 1
                    count = backtrack(board, col + 1, count)
                    # Remove the queen from (row, col)
                    board[row][col] = 0
            return count
    
    def is_valid(board, row, col):
        # Check if there is a queen in the same row
        for i in range(col):
            if board[row][i] == 1:
                return False
        # Check if there is a queen in the same diagonal (upper left to lower right)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        # Check if there is a queen in the same diagonal (lower left to upper right)
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True
    
    # Initialize an empty board
    board = [[0] * n for _ in range(n)]
    # Start backtracking from the first column
    count = backtrack(board, 0, 0)
    return count

# The n_queens function takes an integer n as input
# and returns the number of possible arrangements of n queens
# on an n by n board. The backtrack function recursively tries 
# to place queens in each column, starting from the first column,
# and returns the total number of valid arrangements found.
# The is_valid function checks if it's safe to place a queen at a given 
# position by checking for conflicts with previously placed queens.

# Note that this solution has a time complexity of O(n^n),
# which can be very slow for large values of n. There are more efficient
# algorithms to solve the n-queens problem, such as the Dancing Links algorithm,
# but they are more complex to implement.