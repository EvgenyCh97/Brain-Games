from random import randint

ANSWER_LIST = ['']
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 20


def task():
    random_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    if random_number % 2 == 0:
        ANSWER_LIST[0] = 'yes'
    else:
        ANSWER_LIST[0] = 'no'
    return random_number
