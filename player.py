from game import Game


class Player:
    def __init__(self, username, game_history=[]):
        self.username = username
        self.game_history = game_history

    def add_game(self, game):
        self.game_history.append(game)
        self.game_history()


    def write_game_history(self, game):
        file = open("game_history.txt", "a")
        file.write(f"{game}\n")
        file.close()

    def read_game_history(self):
        try:
            with open("game_history.txt", "r") as file:
                lines = file.readlines()
            for line in lines:
                print(line.rstrip())
        except FileNotFoundError:
            with open("game_history.txt", "w") as file:
                file.write(f"Game history for {self.username}\n")

    def __str__(self):
        return f"{self.username}"

    def print_game_history(self):
        try:
            file = open("game_history.txt", "r")
            for line in file:
                print(line)
        except FileNotFoundError:
            with open("game_history.txt", "w") as file:
                file.write(f"Game history for {self.username}\n")

    def add_test(self, game):
        self.game_history.append(self.username, game)


player = Player("John")
game1 = Game(player.username,"2020-01-02",70, "8:50")
game2 = Game(player.username,"2020-01-03",80, "8:40")
player.write_game_history(game1)
player.print_game_history()
player2 = Player("Mary", 18)
game3= Game(player2.username,"2020-01-04",90, "11:30")
player2.write_game_history(game3)
player2.print_game_history()