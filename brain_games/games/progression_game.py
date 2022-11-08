from random import randint
from brain_games.logic.game_logic import logic

rules = 'What number is missing in the progression?'
answer_list = [0]


def get_progression():
    step_of_progression = randint(2, 4)
    len_of_progression = randint(5, 10)
    elements_count = len_of_progression * step_of_progression
    start_of_progression = randint(0, 100 - elements_count)
    stop_of_progression = start_of_progression + elements_count
    result_list = list(map(str, range(1, 101)[start_of_progression:stop_of_progression:step_of_progression]))
    return result_list


def task():
    progression_list = get_progression()
    random_number_from_list = randint(0, len(progression_list) - 1)
    answer_list[0] = progression_list[random_number_from_list]
    progression_list[random_number_from_list] = '..'
    result = ''
    for char in progression_list:
        if char == progression_list[len(progression_list) - 1]:
            result += char
        else:
            result += char + ' '
    return result


def game():
    logic(rules, task, answer_list)
