from random import randint

ANSWER_LIST = ['']
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBERS_LIST = list(range(1, 21))


def task():
    random_number_index = randint(0, len(NUMBERS_LIST) - 1)
    random_number = NUMBERS_LIST[random_number_index]
    if random_number % 2 == 0:
        ANSWER_LIST[0] = 'yes'
        NUMBERS_LIST.pop(random_number_index)
    else:
        ANSWER_LIST[0] = 'no'
        NUMBERS_LIST.pop(random_number_index)
    return random_number
