from random import randint

RULES = 'What number is missing in the progression?'
ANSWER_LIST = ['']
LIST_OF_NUMBERS = list(map(str, range(1, 101)))


def get_progression_list():
    step_of_progression = randint(2, 4)
    length_of_progression = randint(5, 10)
    elements_count = length_of_progression * step_of_progression
    start_of_progression = randint(0, 100 - elements_count)
    end_of_progression = start_of_progression + elements_count
    trimmed_list_of_numbers = LIST_OF_NUMBERS[start_of_progression:end_of_progression]
    result_list = trimmed_list_of_numbers[::step_of_progression]
    return result_list


def task():
    progression_list = get_progression_list()
    random_number_from_list = randint(0, len(progression_list) - 1)
    ANSWER_LIST[0] = progression_list[random_number_from_list]
    progression_list[random_number_from_list] = '..'
    result = ''
    for char in progression_list:
        if char == progression_list[len(progression_list) - 1]:
            result += char
        else:
            result += char + ' '
    return result
