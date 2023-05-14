from player import Player
from game import Game
from project import check_answer, generate_question

def test_check_answer():
    assert check_answer('2 + 2', '4') == True
    assert check_answer('2 + 2', 'foo') == False

def test_generate_question():
    assert generate_question() !=None
    question = generate_question().split()
    assert question[1] in ['+','-','*','/']
