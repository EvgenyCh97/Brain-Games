from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_task_and_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    divisor = 2
    if random_number == 1:
        return (random_number, 'no')
    while random_number % divisor != 0:
        divisor += 1
    if divisor == random_number:
        return (random_number, 'yes')
    return (random_number, 'no')
