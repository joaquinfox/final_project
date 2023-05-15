
class Player:
    def __init__(self, username):
        self.username = username

    def write_game_history(self, game):
        """Each player objects keeps its own game history. All players share the same game history file."""
        file = open("game_history.txt", "a")
        file.write(f"{game}\n")
        file.close()

    def read_game_history(self) -> None:
        """If a username is not found in the game history file, the user is created and appended to that file."""
        try:
            with open("game_history.txt", "r") as file:
                lines = file.readlines()
            for line in lines:
                print(line.rstrip())
        except FileNotFoundError:
            with open("game_history.txt", "w") as file:
                file.write(f"Game history\n")
        finally:
            file.close()

    def __str__(self):
        return f"{self.username}"

    def print_game_history(self):
        try:
            file = open("game_history.txt", "r")
            for line in file:
                print(line)
        except FileNotFoundError:
            with open("game_history.txt", "w") as file:
                file.write(f"Game history\n")
        finally:
            file.close()
  
