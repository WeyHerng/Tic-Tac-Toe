from Game import Game
from Interface import get_game_type, get_player_markers

def main():
    """Main function to start the game."""
    print("Welcome to Tic-Tac-Toe!")

    game_type = get_game_type()

    if game_type == 'H':
        player1_marker, player2_marker = get_player_markers()
        game = Game(player1_marker, player2_marker, player2_is_ai=False)
    else:
        player1_marker = input("Choose your marker (e.g., X): ").upper()
        game = Game(player1_marker, player2_marker='O', player2_is_ai=True)  # AI always plays 'O'

    game.play()

if __name__ == "__main__":
    main()
