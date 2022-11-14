from random import randint, shuffle

rules = 'What is the result of the expression?'
answer_list = ['']
operator_queue = [1, 2, 3]
shuffle(operator_queue)


def task():
    first_number = randint(1, 20)
    second_number = randint(1, 20)
    if operator_queue[0] == 1:
        answer_list[0] = str(first_number + second_number)
        operator_queue.pop(0)
        return f'{first_number} + {second_number}'
    elif operator_queue[0] == 2:
        answer_list[0] = str(first_number - second_number)
        operator_queue.pop(0)
        return f'{first_number} - {second_number}'
    else:
        answer_list[0] = str(first_number * second_number)
        operator_queue.pop(0)
        return f'{first_number} * {second_number}'
