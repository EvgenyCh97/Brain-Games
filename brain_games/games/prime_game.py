from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ANSWER_LIST = ['']
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 20


def task():
    random_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    divisor = 2
    if random_number == 1:
        ANSWER_LIST[0] = 'no'
        return random_number
    while random_number % divisor != 0:
        divisor += 1
    if divisor == random_number:
        ANSWER_LIST[0] = 'yes'
        return random_number
    ANSWER_LIST[0] = 'no'
    return random_number
