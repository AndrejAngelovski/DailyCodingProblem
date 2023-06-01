import heapq

class Puzzle:
    def __init__(self, board):
        self.board = board
        self.string = str(self.board)
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    self.empty_spot = (i, j)

    def moves(self):
        i, j = self.empty_spot
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = i + dx, j + dy
            if 0 <= x < 3 and 0 <= y < 3:
                board = [row[:] for row in self.board]
                board[i][j] = board[x][y]
                board[x][y] = None
                yield Puzzle(board)

    def heuristic(self):
        return sum(abs(i // 3 - x) + abs(i % 3 - y)
            for i, row in enumerate(self.board)
            for j, val in enumerate(row) if val is not None
            for x in range(3) for y in range(3) if self.board[x][y] == val)

    def __lt__(self, other):
        return False

def solve(board):
    start = Puzzle(board)
    queue = [(start.heuristic(), start)]
    visited = {start.string}

    while queue:
        _, cur = heapq.heappop(queue)
        if cur.board == [[1, 2, 3], [4, 5, 6], [7, 8, None]]:
            return cur.board
        for next_board in cur.moves():
            if next_board.string not in visited:
                visited.add(next_board.string)
                heapq.heappush(queue, (next_board.heuristic(), next_board))
    return None

print(solve([[5, 1, 3], [None, 2, 6], [4, 7, 8]]))
