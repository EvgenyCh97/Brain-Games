from random import randint

RULES = 'What number is missing in the progression?'
MIN_ARITHMETIC_DIFFERENCE = 1
MAX_ARITHMETIC_DIFFERENCE = 4
MIN_NUMBER_OF_DIGITS = 5
MAX_NUMBER_OF_DIGITS = 10
RANGE_START = 0
RANGE_END = 100


def get_progression_list():
    step = randint(MIN_ARITHMETIC_DIFFERENCE, MAX_ARITHMETIC_DIFFERENCE)
    number_of_digits = randint(MIN_NUMBER_OF_DIGITS, MAX_NUMBER_OF_DIGITS)
    start_of_progression = randint(RANGE_START, RANGE_END)
    list_of_numbers = []
    index = 0
    while len(list_of_numbers) != number_of_digits:
        element = start_of_progression + index * step
        list_of_numbers.append(element)
        index += 1
    result_list = list(map(str, list_of_numbers))
    return result_list


def task():
    progression_list = get_progression_list()
    random_number_from_list = randint(0, len(progression_list) - 1)
    correct_answer = progression_list[random_number_from_list]
    progression_list[random_number_from_list] = '..'
    question = ''
    for char in progression_list:
        if char == progression_list[len(progression_list) - 1]:
            question += char
        else:
            question += char + ' '
    return (question, correct_answer)
