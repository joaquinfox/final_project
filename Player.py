class Player:
    def __init__(self, username):
        self.username = username
        self.games = {}

    def add_game(self, date, game_level, score, time):
        game = {'username': self.username, 'date': date, 'game_level': game_level, 'score': score, 'time': time}
        self.games[date] = game

    def get_high_score(self, game_level):
        high_score = 0
        for game in self.games.values():
            if game['game_level'] == game_level and game['score'] > high_score:
                high_score = game['score']
        return high_score



        '''
        class Player has two attributes a username and games. username is a unique string. games is a dictionary of game items. each game item in the dictionary has the following keys:
            username, date, game_level, score, time
        '''

