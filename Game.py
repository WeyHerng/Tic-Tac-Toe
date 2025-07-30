
from Board import Board
from Player import Player

class Game:
    def __init__(self, player1_marker='X', player2_marker='O', player2_is_ai=False):
        self.board = Board()
        self.player1 = Player(player1_marker)
        self.player2 = Player(player2_marker, is_human=not player2_is_ai)  # Player 2 can be AI
        self.current_player = self.player1

    def switch_player(self):
        """Switches the current player."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        """Main game loop."""
        while True:
            self.board.display()
            row, col = self.current_player.get_move(self.board)

            if self.board.make_move(row, col, self.current_player):
                if self.board.check_win(self.current_player):
                    self.board.display()
                    print(f"Player {self.current_player.marker} wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()
            else:
                print("Invalid move. Try again.")