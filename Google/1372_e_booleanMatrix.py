# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you
# can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum
# number of steps required to reach the end coordinate from the start. If there is 
# no possible path, then return null. You can move up, left, down, and right. You 
# cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]

# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
# of steps required to reach the end is 7, since we would need to go through (1, 2)
# because there is a wall everywhere else on the second row.

def min_steps_to_reach_end(board, start, end):
    m, n = len(board), len(board[0])
    q = [(start, 0)] # queue of (tile, distance) tuples
    visited = set([start]) # set of visited tiles
    while q:
        tile, dist = q.pop(0)
        if tile == end:
            return dist
        row, col = tile
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = row + dr, col + dc
            if 0 <= r < m and 0 <= c < n and not board[r][c] and (r, c) not in visited:
                q.append(((r, c), dist + 1))
                visited.add((r, c))
    return None

board = [[False, False, False, False],
         [True, True, False, True],
         [False, False, False, False],
         [False, False, False, False]]

start = (3, 0)
end = (0, 0)
print(min_steps_to_reach_end(board, start, end))
