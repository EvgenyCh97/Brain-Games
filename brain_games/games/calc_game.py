from random import randint, shuffle

RULES = 'What is the result of the expression?'
ANSWER_LIST = ['']
OPERATOR_QUEUE = [1, 2, 3]
shuffle(OPERATOR_QUEUE)
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 20


def task():
    first_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    second_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    if OPERATOR_QUEUE[0] == 1:
        ANSWER_LIST[0] = str(first_number + second_number)
        OPERATOR_QUEUE.pop(0)
        return f'{first_number} + {second_number}'
    elif OPERATOR_QUEUE[0] == 2:
        ANSWER_LIST[0] = str(first_number - second_number)
        OPERATOR_QUEUE.pop(0)
        return f'{first_number} - {second_number}'
    else:
        ANSWER_LIST[0] = str(first_number * second_number)
        OPERATOR_QUEUE.pop(0)
        return f'{first_number} * {second_number}'
