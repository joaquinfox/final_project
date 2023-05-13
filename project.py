from player import Player
from game import Game
import re, datetime


def main():
    username: str = get_username()
    counter = 0
    score_card = 0
    while counter < 10:
        question = generate_question()
        print(question)
        counter += 1
        answer = input("Answer: ").strip()
        if check_answer(answer):
            score_card += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print(f"Your score is {score_card}")


def get_username() -> str:
    return input("Username: ")


def generate_question() -> str:
    return "foo"


def check_answer(answer: str) -> bool:
    return True

def timer():
    pass

def get_date():
    pass


if __name__ == "__main__":
    main()
