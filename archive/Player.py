import Game
class Player:
    def __init__(self, username):
        self.username = username
        self.games = {}
    


    def add_game(self, date, game_level, score, time):
        game = Game(self.username, date, game_level, score, time)
        self.games[date] = game


    def print_games(self):
        for game in self.games.values():
            game.print_game()
            # print(game)

        '''
        class Player has two attributes a username and games. username is a unique string. games is a dictionary of game items. each game item in the dictionary has the following keys:
            username, date, game_level, score, time
        '''

# add object to a dictionary
# https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary