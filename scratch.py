import Game
import Player
import time
import msvcrt
import sys


# def question_timer(s: int) -> None:
#     for remaining in range(s, 0, -1):
#         print(f"\033[1;31m {remaining} seconds\033[0m  ", end='', flush=True)
#         start_time = time.monotonic()
#         while time.monotonic() < start_time + 1:
#             if msvcrt.kbhit() and msvcrt.getch() == '1':
#                 print("\033[1mYou entered 1. Timer stopped.\033[0m")
#                 return
#     print("\033[1mTime is up.\033[0m")

# question_timer(10)

test_player = Player("test_player")
game1 = Game("test_player", "2021-01-01", 1, 100, 10)
# test_player.add_game(game1)
# game2 = Game("test_player", "2021-01-02", 2, 200, 20)
# test_player.add_game(game2)
# test_player.add_game("2021-01-02", 2, 200, 20)
# test_player.add_game("2021-01-03", 3, 300, 30)

# test_player.print_games()
# print(test_player.games)
# import time
# def question_timer(s: int) -> None:
#     for remaining in range(s, -1, -1):
#         sys.stdout.write(f"\033[1;31m {remaining} seconds\033[0m  ")
#         sys.stdout.flush()
#         time.sleep(1)
#         sys.stdout.write('\r')
#         sys.stdout.flush()
#         answer = input("Enter your answer: ")
#         if answer == "1":
#             print("You entered 1. Timer stopped.")
#             break

# question_timer(10)