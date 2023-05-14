Math Hero (MH)
A math game for learning arithmetic at a first grade level.
What does it do?
MH generates a game of 10 questions, scores the results, and persists the results to a file.

MVP Story line
User can:
- execute math_hero.py from a command line
- Is prompted to input username on the command line.
- User recieves a question on the CL
- User inputs and answer and hits enter to submit
- Question is evaluated and right wrong feedback is printed to the screen
- the next question is printed
- when 10 question have been completed, game stats are written to the game_history file and game stats are printed to the terminal

The program  builds a game of (default length) 10 questions, and presents the questions one at a time. On answering correctly or incorrectly (with time remaining) the game generates some user feedback. TODO: What kind of feedback?

MH further, returns a user score, and persists results to a file, with the date of the game, a user name, and a score. User is able to retrieve and print their game history.

MVP: game interface will be the command line. Game parameters will be entered as argument flags on the CL. Questions will be printed to the CL and responses as well. User will answer via CL.



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

CLASSES:
Class Player
    Attributes
    - name
    - game history
         list of games played
    Methods
    - add_game(): appends a game instance to a list
    - write_game_history(): writes a new game to file
    - read_game_history(): reads the current history on file
    - print_game_history():

Class Game
    Attributes
    - username
    - time: time taken to complete the game
    - date of game
    - score of game


General:
The program uses the two objects above. Class Game encapsulates game stats which are stored in a list, as an attribute of the Player instance.

Game execution is handled in a series of procedural functions, inside of main(). 

Class Player organizes game results for file write.


Introduction:
Welcome to Math Hero!
Choose a username. We will build you a ten question game. Answer as many as you can, as fast as you can, and we will score you, and track your game performance.

EXTENSIONS:
- Format output of duration
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
