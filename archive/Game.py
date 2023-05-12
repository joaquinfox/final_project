import datetime
class Game:

    def __init__(self, username, date, game_level, score, time):
        self.username = username
        self.date = date
        self.game_level = game_level
        self.score = score
        self.time = time
# getters for all attributes?
    def get_username(self):
        return self.username
    def get_date(self):
        return self.date
    def get_game_level(self):
        return self.game_level
    def get_score(self):
        return self.score
    def get_time(self):        
        return self.time    
# setters for all attributes?
    def set_username(self, username):
        self.username = username
    def set_date(self, date):
        self.date = date
    def set_game_level(self, game_level):
        self.game_level = game_level
    def set_score(self, score):
        self.score = score
    def set_time(self, time):
        self.time = time

    def start(self):
        self.start_time = datetime.datetime.now()
    def end(self):
        self.end_time = datetime.datetime.now()
        self.time = self.end_time - self.start_time

    def __str__(self):  
        return f"{self.username} played on {self.date} at level {self.game_level} and scored {self.score} in {self.time} seconds."

        # how do i call this method?
    def print_game(self):   
        print(f"{self.username} played on {self.date} at level {self.game_level} and scored {self.score} in {self.time} seconds.")
    