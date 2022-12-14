from random import randint, choice
from operator import add, mul, sub

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 20


def calculate_result(first_number, second_number, operator):
    return operator(first_number, second_number)


def get_task_and_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice((add, mul, sub))
    result = str(calculate_result(first_number, second_number, operator))
    if operator == add:
        question = f'{first_number} + {second_number}'
        return (question, result)
    elif operator == sub:
        question = f'{first_number} - {second_number}'
        return (question, result)
    else:
        question = f'{first_number} * {second_number}'
        return (question, result)
