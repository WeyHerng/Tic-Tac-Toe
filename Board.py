
class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]  # Initialize with empty spaces

    def display(self):
        """Prints the board to the console."""
        for row in self.grid:
            print("|" + "|".join(row) + "|")
        print("-" * (self.size * 2 + 1))

    def is_valid_move(self, row, col):
        """Checks if a move is within bounds and the cell is empty."""
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == ' '

    def make_move(self, row, col, player):
        """Places the player's mark on the board."""
        if self.is_valid_move(row, col):
            self.grid[row][col] = player.marker
            return True
        return False

    def is_full(self):
        """Checks if the board is full."""
        for row in self.grid:
            if ' ' in row:
                return False
        return True

    def get_empty_cells(self):
        """Returns a list of (row, col) tuples representing empty cells."""
        empty_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == ' ':
                    empty_cells.append((row, col))
        return empty_cells

    def check_win(self, player):
        """Checks if the given player has won."""
        marker = player.marker

        # Check rows
        for row in self.grid:
            if all(cell == marker for cell in row):
                return True

        # Check columns
        for col in range(self.size):
            if all(self.grid[row][col] == marker for row in range(self.size)):
                return True

        # Check diagonals
        if all(self.grid[i][i] == marker for i in range(self.size)):
            return True
        if all(self.grid[i][self.size - 1 - i] == marker for i in range(self.size)):
            return True

        return False