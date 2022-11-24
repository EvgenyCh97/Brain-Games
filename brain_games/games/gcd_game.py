from random import randint
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 10


def get_task_and_answer():
    first_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    second_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return (question, correct_answer)
