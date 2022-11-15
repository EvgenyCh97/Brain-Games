from random import randint

rules = 'What number is missing in the progression?'
answer_list = ['']


def get_progression_list():
    progression_step = randint(2, 4)
    progression_len = randint(5, 10)
    elements_count = progression_len * progression_step
    progression_start = randint(0, 100 - elements_count)
    progression_stop = progression_start + elements_count
    str_list = list(map(str, range(1, 101)))
    result_list = str_list[progression_start:progression_stop:progression_step]
    return result_list


def task():
    progression_list = get_progression_list()
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
