from random import randint
from brain_games.logic.game_logic import logic

answer_list = ['']
rules = 'Answer "yes" if the number is even, otherwise answer "no".'
numbers_list = list(range(1, 21))


def task():
    random_number_index = randint(0, len(numbers_list) - 1)
    random_number = numbers_list[random_number_index]
    if random_number % 2 == 0:
        answer_list[0] = 'yes'
        numbers_list.pop(random_number_index)
    else:
        answer_list[0] = 'no'
        numbers_list.pop(random_number_index)
    return random_number


def game():
    logic(rules, task, answer_list)
