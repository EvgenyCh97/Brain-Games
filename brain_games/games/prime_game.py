from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 20


def task():
    random_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    divisor = 2
    if random_number == 1:
        return (random_number, 'no')
    while random_number % divisor != 0:
        divisor += 1
    if divisor == random_number:
        return (random_number, 'yes')
    return (random_number, 'no')
