from player import Player
from game import Game
from project import check_answer, generate_question, calc_duration
import datetime

def test_check_answer():
    assert check_answer('2 + 2', '4') == True
    assert check_answer('2 + 2', 'foo') == False

def test_generate_question():
    assert generate_question() !=None
    question = generate_question().split()
    assert question[1] in ['+','-','*','/']

def test_calc_duration():
    dt1 = datetime.datetime(2023,1,1,12,30,0)
    dt2 = datetime.datetime(2023,1,1,12,30,10)
    a,b = (calc_duration(dt1, dt2))
    assert a == 0
    assert b == 10