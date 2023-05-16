# Math Hero (MH)
#### Video Demo: https://youtu.be/3gXcUi3Udkc
#### Description
MH is a tool to learn math, inspired by my own kid's reckoning with math. My goal was to build a fun, simple interface to practice tons of math problems, and while this version is low on the "fun" gradient, the proof of concept is, I think, a promissing foundation on which to build more intricate and graphically engaging games. The program generates a game of 10 questions, scores the results, and persists game stats to a file. The game interface is the command line. Game execution is controlled from main() which calls helper functions to generate random questions and check answers.

After the final question is answered, two custom objects are instantiated, a Game object which encapsulates game data, and a Player object, which encapsulates the file read and write functionality.
Class methods are then called to perform the file IO.

#### MVP
The user can
- execute math_hero.py from a command line
- input username on the command line.
- receive a question on the CL
- inputs an answer 
- see right wrong feedback printed to the screen
- when 10 question have been completed, game stats are written to the game_history file and game stats are printed to the terminal

#### Code Structure

GAMEFLOW                                           LOGIC
- execute mathmonster.py                            CL
- get user name                                     get_username
- generate a question                               geneate_question()
- start game timer                                  timer()
- print questions and handle input                  play_game()
- evaluate each answer                              check_answer()
- print feedback                                    main()
- When game is over, 
        - get game duration                         timer()
        - get date                                  get_date()
        - Instantiate a Player with the username    main() 
        - Instantiate a Game instance               main()
        - write game to file                        Class method write_game_history
        - print game stats                          Class method print_game_history 

#### CLASSES:
Class Player
    Attributes
    - name
    Methods
    - write_game_history(): writes a new game to file
    - read_game_history(): reads the current history on file
    - print_game_history():

Class Game
    Attributes
    - username
    - time: time taken to complete the game
    - date of game
    - score of game

#### EXTENSIONS:...for another day
- Add a time limit for each question, and some kind of graphical count down or spinner feature
- Returning players get a print out of their game stats when the program is launched.
- first time players get some introductory information about the game, presented in tabular form in the CL
- Allow user to select difficulty levels 1-3 and generates a game of math problems at that level. Add a level attribute to class Game. 
Questions are built around the four basic operators +, -, * and /.
Difficulty is increased by increasing integer sizes, single, double or triple digit.

Difficulty         Example problems at each level
Operator     1                      2               3 
===========================================================
+          2 + 4                 22 + 17          235 + 178
-          4 - 5 | 5 - 4         22 - 17          435 - 852
*          2 * 8                 22 * 8           225 * 8
/          8 / 4                 8 / 4 | 4 / 8    22 / 4 


 - Build out web/desktop interfaces, with more graphical capabiliites.
 - move game logic from main() to class Game
