Math Monster (Math Hero?)
A math game for learning arithmitec at a first grade level.
What does it do?
MM allows a user to select difficulty levels 1-3 and generates a game of math problems at that level. Game time and other stats are tracked and  persisted to a file (automatically)

TODO: When/how can user access game history? 
    - Returning players get a print out of their game stats when the program is launched.
    - first time players get some introductory information about the game, presented in tabular form in the CL

TODO: MVP difficulty level can be specified as command line argument, or if no argument is provided, as a string at the input prompt. 
    EXTENSION: add settings for game length, and problem types (+ , - , * , /). 
    EXTENSION: add web/desktop interface.

The program then builds a game of (default length) 10 questions, and presents the questions one at a time. On answering correctly or incorrectly (with time remaining) the game generates some user feedback.


EXTENSION: make game length variable on user input

Questions are built around the four basic operators +, -, * and /.
Difficulty is increased by increasing integer sizes, single, double or triple digit.

Difficulty   1                      2               3
Operator     Example problems at each level
===========================================================
+          2 + 4                 22 + 17          235 + 178
-          4 - 5 | 5 - 4         22 - 17          435 - 852
*          2 * 8                 22 * 8           225 * 8
/          8 / 4                 8 / 4 | 4 / 8    22 / 4 


MM further, returns a user score, and persists results to a file, with the date of the game, a user name, and a score. User is able to retrieve and print their game history.

MVP: game interface will be the command line. Game parameters will be entered as argument flags on the CL. Questions will be printed to the CL and responses as well. User will answer via CL.
How will a timer be implemented? 
RESEARCH:
- CL timer
- CL arguments


GAMEFLOW                                           LOGIC
- execute mathmonster.py                            CL
SETUP
- get user name
- choose difficulty level 1 - 3                     get_level
- generate question set                             get_set
- re-set new game                                   reset
- write game score                                  log_game
GAME PLAY
- present questions with a timer, user messaging    game_controller 
- evaluate question                                 grade_problem
- reset timer                                       timer
                                  

OBJECTS AND CLASSES:
Class Player
    - name
    - game stats list of games played
        - 

Class Game
    - level of game
    - time: time taken to complete the game
    - date of game
    - score of game

General:
The program uses the two objects above. Class Game contains the logic to generate the problem set based on inputed difficulty.

Game execution is handled in a series of procedural functions.

Class Player organizes game results for file write.

LOG 5/9/23
Using the CL and spinner libraries is proving hard to use for the game design. Rethinking this.
When process runs:
- prompt name
- prompt level
generate game, instantiate objects then
- present a counter TODO
- print question
- prompt answer
if answer is wrong and time remains
    continue
if answer is right
    next question
LOG 5/10/23
Abandoning the timer feature. Too hard to implement a cl timer, while also prompting for user input, the two features overwrite eachother or interfere in other ways.
New game-flow:
- prompt for name and level
- present questions in sequence, without time limit.
- instead of a timer, track time and print total time at end.
- print a welcome sign

Welcome to Math Hero!
Choose a username and choose a level. We will build you a ten question game. Answer as many as you can, as fast as you can, and we will score you


TTD