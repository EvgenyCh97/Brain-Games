from random import randint

RULES = 'Find the greatest common divisor of given numbers.'
ANSWER_LIST = ['']


def task():
    first_given_number = randint(1, 10)
    second_given_number = randint(1, 10)
    question_list = [first_given_number, second_given_number]
    while first_given_number != 0 and second_given_number != 0:
        if first_given_number > second_given_number:
            first_given_number = first_given_number % second_given_number
        else:
            second_given_number = second_given_number % first_given_number
    ANSWER_LIST[0] = str(first_given_number + second_given_number)
    return f'{question_list[0]} {question_list[1]}'
