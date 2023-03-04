# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting
# at the top-left corner and getting to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right

def count_paths(N, M):
    if N == 1 or M == 1:
        return 1
    
    # Create a 2D array of zeroes to store the path counts
    path_counts = [[0 for j in range(M)] for i in range(N)]

    # Set the path count to 1 for the first row and column
    for i in range(N):
        path_counts[i][0] = 1
    for j in range(M):
        path_counts[0][j] = 1
    
    # Compute the path counts for the rest of the matrix
    for i in range(1, N):
        for j in range(1, M):
            path_counts[i][j] = path_counts[i-1][j] + path_counts[i][j-1]

    # Return the path count for the bottom-right corner
    return path_counts[N-1][M-1]

# The count_paths function uses dynamic programming to compute 
# the number of ways to get from the top-left corner to the bottom-
# right corner of the matrix. It first checks if either N or M is 1,
# in which case there is only one way to get to the bottom-right 
# corner. Otherwise, it creates a 2D array of zeros to store the path 
# counts, sets the path count to 1 for the first row and column 
# (since there is only one way to get to any cell in those rows and
#   columns), and then computes the path counts for the rest of the
# matrix by summing the path counts for the cell above and the cell
# to the left.

N = int(input())
M = int(input())
num_paths = count_paths(N, M)
print(num_paths)