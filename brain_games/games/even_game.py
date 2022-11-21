from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 20


def task():
    random_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    if random_number % 2 == 0:
        return (random_number, 'yes')
    else:
        return (random_number, 'no')
