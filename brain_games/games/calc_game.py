from random import randint, shuffle

RULES = 'What is the result of the expression?'
ANSWER_LIST = ['']
OPERATOR_QUEUE = [1, 2, 3]
shuffle(OPERATOR_QUEUE)


def task():
    first_given_number = randint(1, 20)
    second_given_number = randint(1, 20)
    if OPERATOR_QUEUE[0] == 1:
        ANSWER_LIST[0] = str(first_given_number + second_given_number)
        OPERATOR_QUEUE.pop(0)
        return f'{first_given_number} + {second_given_number}'
    elif OPERATOR_QUEUE[0] == 2:
        ANSWER_LIST[0] = str(first_given_number - second_given_number)
        OPERATOR_QUEUE.pop(0)
        return f'{first_given_number} - {second_given_number}'
    else:
        ANSWER_LIST[0] = str(first_given_number * second_given_number)
        OPERATOR_QUEUE.pop(0)
        return f'{first_given_number} * {second_given_number}'
