from random import randint

RULES = 'Find the greatest common divisor of given numbers.'
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 10


def task():
    first_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    second_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    question = f'{first_number} {second_number}'
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    correct_answer = str(first_number + second_number)
    return (question, correct_answer)
