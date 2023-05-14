from player import Player
from game import Game
import datetime, random


def main():
    username: str = get_username()
    counter = 0
    score_card = 0
    game_duration = 0
    start = datetime.datetime.now()
    while counter < 10:
        question = generate_question()
        print(question)
        counter += 1
        try:
            answer = (input("Answer: ").strip())
            if check_answer(question, answer):
                score_card += 1
                print("Correct!")
            else:
                print("Incorrect!")
        except ValueError:
            print("Incorrect!")
            continue
        except ZeroDivisionError:
            print("Incorrect!")
            continue
    end = datetime.datetime.now()
    game_duration = end - start
    total_seconds = game_duration.total_seconds()
    minutes =int(total_seconds /60)
    seconds = int(total_seconds % 60)
    game_duration =f"{minutes}:{seconds}"
    print(f'game_duration: {minutes}:{seconds}')
    print(f"Your score is {score_card}")

    player = Player(username)
    game = Game(username, datetime.datetime.now().strftime("%Y-%m-%d"), score_card, str(game_duration))
    player.read_game_history()
    player.write_game_history(game) # write game to file
    player.print_game_history() # print game history



def get_username() -> str:
    return input("Username: ")


def generate_question() -> str:
    a = random.randint(-9, 9)
    b = random.randint(-9, 9)
    c = random.randint(1, 4)
    operators = {1: "+", 2: "-", 3: "*", 4: "/"}
    operator = operators[c]
    if c == 4.0 and b == 0: # prevent division by zero
        b = random.randint(1, 9)
    return f"{a} {operator} {b}"


def check_answer(question: str, answer: str) -> bool:
    correct_answer = eval(question)
    rounded_answer = round(correct_answer, 4) # round() creates a float 
    # print('LOG', rounded_answer, answer)
    if float(answer) != rounded_answer:
        return False
    return True




if __name__ == "__main__":
    main()
