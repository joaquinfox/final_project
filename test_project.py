from player import Player
from game import Game
# from project import TODO

def test_add_game_to_history():
    # Create a Player object
    player = Player("John")

    # Create a Game object
    game = Game(player.username,"2020-01-02",70, "8:50")

    # Add the Game to the Player's history
    player.add_game(game)

    # Check that the Player's history contains the Game
    assert game in player.game_history

def test_read_game_history():
    # Create a Player object
    player = Player("John")

    # Create a Game object
    game = Game(player.username,"2020-01-02",70, "8:50")

    # Add the Game to the Player's history
    player.add_game(game)

    # Read the Player's history from file
    player.read_game_history()

    # Check that the history was read correctly
    assert f"{game}\n" in capsys.readouterr().out

In this example, the first test checks that the add_game() method adds a Game object to the Player's history list, and the second test checks that the read_game_history() method reads the Player's history from file and prints it to the console correctly.

You can run the test file with the pytest command in the terminal.
