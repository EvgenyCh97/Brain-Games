from random import randint
from brain_games.logic.game_logic import logic

answer_list = [0]
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def task():
    random_number = randint(1, 20)
    if random_number % 2 == 0:
        answer_list[0] = 'yes'
    else:
        answer_list[0] = 'no'
    return random_number


def game():
    logic(rules, task, answer_list)
