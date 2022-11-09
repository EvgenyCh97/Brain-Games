from random import randint
from brain_games.logic.game_logic import logic

rules = 'Find the greatest common divisor of given numbers.'
answer_list = ['']


def task():
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    question_list = [first_number, second_number]
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    answer_list[0] = str(first_number + second_number)
    return f'{question_list[0]} {question_list[1]}'


def game():
    logic(rules, task, answer_list)
