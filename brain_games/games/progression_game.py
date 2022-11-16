from random import randint

RULES = 'What number is missing in the progression?'
ANSWER_LIST = ['']
MINIMUM_ARITHMETIC_DIFFERENCE = 1
MINIMUM_NUMBER_OF_DIGITS = 5


def get_progression_list():
    number_of_digits = MINIMUM_NUMBER_OF_DIGITS + randint(0, 5)
    arithmetic_difference = MINIMUM_ARITHMETIC_DIFFERENCE + randint(1, 3)
    start_of_progression = randint(0, 100)
    list_of_numbers = []
    index = 0
    while len(list_of_numbers) != number_of_digits:
        progression_element = start_of_progression + index * arithmetic_difference
        list_of_numbers.append(progression_element)
        index += 1
    result_list = list(map(str, list_of_numbers))
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
