class Player:
    def __init__(self, marker, is_human=True):
        self.marker = marker
        self.is_human = is_human

    def get_move(self, board):
        """Gets the player's move.  If human, prompts for input.  If AI, uses an AI algorithm."""
        if self.is_human:
            return self.get_human_move(board)
        else:
            return self.get_ai_move(board)  # Placeholder for AI logic

    def get_human_move(self, board):
        """Prompts the human player for a move."""
        while True:
            try:
                row = int(input(f"Player {self.marker}, enter row (0-{board.size - 1}): "))
                col = int(input(f"Player {self.marker}, enter column (0-{board.size - 1}): "))
                if board.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input.  Enter numbers.")

    def get_ai_move(self, board):
        """Placeholder for AI move logic.  Replace with an actual AI algorithm."""
        # Simple random move for now
        import random
        empty_cells = board.get_empty_cells()
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return None  # Board is full (shouldn't happen if called correctly)
