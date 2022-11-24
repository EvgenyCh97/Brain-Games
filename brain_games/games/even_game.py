from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_task_and_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if random_number % 2 == 0:
        return (random_number, 'yes')
    else:
        return (random_number, 'no')
