class Test:
    def __init__(self, username, date: str, score: int, test_duration: str = ""):
        self.username = username
        self.date = date
        self.score = score
        self.test_duration = test_duration.split(":")

    def __str__(self):
        return f"Test stats:\n\tPlayer: {self.username}, Date: {self.date}, score: {self.score}, time taken: {self.test_duration}"


# game1 = Test("2020-01-02",70, "8:40")
