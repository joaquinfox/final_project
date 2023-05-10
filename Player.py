class Game:
    def __init__(self, username, date, game_level, score, time):
        self.username = username
        self.date = date
        self.game_level = game_level
        self.score = score
        self.time = time

class Player:
    def __init__(self, username):
        self.username = username
        self.games = {}

    def add_game(self, date, game_level, score, time):
        game = Game(self.username, date, game_level, score, time)
        self.games[date] = game




        '''
        class Player has two attributes a username and games. username is a unique string. games is a dictionary of game items. each game item in the dictionary has the following keys:
            username, date, game_level, score, time
        '''

