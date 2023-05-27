# Connect 4 is a game where opponents take turns dropping
# red or black discs into a 7 x 6 vertically suspended grid. 
# The game ends either when one player creates a line of four
# consecutive discs of their color (horizontally, vertically, 
# or diagonally), or when there are no more spots left in the grid.

# Design and implement Connect 4.

class Connect4:
    def __init__(self):
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.current_player = "Red"
    
    def drop_disc(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] is None:
                self.board[row][column] = self.current_player
                if self.check_win(row, column):
                    return f"{self.current_player} wins!"
                self.current_player = "Black" if self.current_player == "Red" else "Red"
                return "Disc placed successfully"
            return "Column is full"
    
    def check_win(self, row, column):
        color = self.board[row][column]
        for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
            if self.count_consecutive(row, column, dx, dy, color) + \
               self.count_consecutive(row, column, -dx, -dy, color) - 1 >= 4:
                return True
            return False
    
    def count_consecutive(self, row, column, dx, dy, color):
        count = 0
        while 0 <= row < 6 and 0 <= column < 7 and self.board[row][column] == color:
            count += 1
            row += dx
            column += dy
        return count