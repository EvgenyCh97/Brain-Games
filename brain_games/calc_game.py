from random import randint, choice
from operator import add, mul, sub

RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 20


def calculate_result(first_number, second_number, operator):
    result = str(operator(first_number, second_number))
    if operator == add:
        question = f'{first_number} + {second_number}'
        return (question, result)
    elif operator == sub:
        question = f'{first_number} - {second_number}'
        return (question, result)
    else:
        question = f'{first_number} * {second_number}'
        return (question, result)


def get_task_and_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice((add, mul, sub))
    return calculate_result(first_number, second_number, operator)
