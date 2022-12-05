from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 20


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_task_and_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(random_number):
        return (random_number, 'yes')
    else:
        return (random_number, 'no')
