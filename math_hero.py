# TODO class Player
# TODO class Game
# TODO build_game
# TODO play_game
import re

def main():
    players = ["bob", "blue", "boo"]
    game_setup(players)
    ...


def game_setup(players):
    player = get_username(players)
    level = get_level()
    build_game(level)
    # TODO: build Player obj
    # TODO: build Game obj
    print("LOG", level)


def get_username(players: str) -> str:
    """
    :param players: list of usernames
    :type players: list of str
    :return: username
    :rtype: str
    """
    username = input("Username: ")
    if username not in players:
        players.append(username)
        # TODO print_welcome(new)
    else:
        # TODO print_welcom(old)
        ...
    return username


def get_level() -> int:
    """
    :return: level
    :rtype: int
    """
    while True:
        pattern = r"(1|2|3)"
        level = input("Level (1 - 3): ")  # TODO validate level
        if matches := re.search(pattern, level):
            break
    return int(level)


def build_game(l: int):
    '''
    takes a level and builds a game object, then calls play_game with that object'''
    ...


if __name__ == "__main__":
    main()
