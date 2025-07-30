# cli.py
def get_game_type():
    """Asks the user if they want to play against another human or the AI."""
    while True:
        choice = input("Play against another human (H) or the AI (A)? (H/A): ").upper()
        if choice in ('H', 'A'):
            return choice
        else:
            print("Invalid choice. Please enter 'H' or 'A'.")

def get_player_markers():
    """Asks the user for the markers they want to use."""
    while True:
        marker1 = input("Player 1, choose your marker (e.g., X): ").upper()
        if len(marker1) == 1:
            break
        else:
            print("Marker must be a single character.")

    while True:
        marker2 = input("Player 2, choose your marker (e.g., O): ").upper()
        if len(marker2) == 1 and marker2 != marker1:
            break
        else:
            print("Marker must be a single character and different from Player 1's marker.")

    return marker1, marker2