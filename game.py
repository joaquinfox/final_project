class Game:
    def __init__(self, username, date: str, score: int, game_duration: str = ""):
        self.username = username
        self.date = date
        self.score = score
        self.game_duration = game_duration

    def __str__(self):
        return f"game stats for {self.username}:\n\t Date: {self.date}, score: {self.score}, time taken: {self.game_duration}"


