from random import randint

DESCRIPTION = 'What number is missing in the progression?'
MIN_ARITHMETIC_DIFFERENCE = 1
MAX_ARITHMETIC_DIFFERENCE = 4
MIN_NUMBER_OF_DIGITS = 5
MAX_NUMBER_OF_DIGITS = 10
RANGE_START = 0
RANGE_END = 100


def get_progression_list(step, number_of_digits, start_of_progression):
    stop = start_of_progression + (number_of_digits * step)
    numbers_list = range(start_of_progression, stop, step)
    return list(map(str, numbers_list))


def get_task_and_answer():
    step = randint(MIN_ARITHMETIC_DIFFERENCE, MAX_ARITHMETIC_DIFFERENCE)
    number_of_digits = randint(MIN_NUMBER_OF_DIGITS, MAX_NUMBER_OF_DIGITS)
    start = randint(RANGE_START, RANGE_END)
    progression_list = get_progression_list(step, number_of_digits, start)
    random_number_from_list = randint(0, len(progression_list) - 1)
    correct_answer = progression_list[random_number_from_list]
    progression_list[random_number_from_list] = '..'
    question = ' '.join(progression_list)
    return (question, correct_answer)
