import time

# duration = 10 # seconds
'''
:param s: time allowed per question, in seconds
:raise TypeError : if s is not an int
:rtype: None
'''

def question_timer(s: int) -> None:
    # try:
        for remaining in range(1,s + 1,1):
            print(f"\033[1;31m {remaining} seconds\033[0m  ", end='')
            time.sleep(1)
            print('\r', end='')
            answer = input("answer: ")
            if answer == "1":
                break
    # except KeyboardInterrupt:
    #     pass

question_timer(10)