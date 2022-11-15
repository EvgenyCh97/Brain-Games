from random import randint

ANSWER_LIST = ['']
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def task():
    random_number = randint(1, 20)
    if random_number % 2 == 0:
        ANSWER_LIST[0] = 'yes'
    else:
        ANSWER_LIST[0] = 'no'
    return random_number
