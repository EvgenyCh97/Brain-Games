from random import randint

RULES = 'What is the result of the expression?'
MIN_GIVEN_NUMBER = 1
MAX_GIVEN_NUMBER = 20


def get_task_and_answer():
    first_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    second_number = randint(MIN_GIVEN_NUMBER, MAX_GIVEN_NUMBER)
    if first_number + second_number < MAX_GIVEN_NUMBER:
        question = f'{first_number} * {second_number}'
        correct_answer = str(first_number * second_number)
        return (question, correct_answer)
    else:
        if first_number >= second_number:
            question = f'{first_number} - {second_number}'
            correct_answer = str(first_number - second_number)
            return (question, correct_answer)
        elif second_number > first_number:
            question = f'{first_number} + {second_number}'
            correct_answer = str(first_number + second_number)
            return (question, correct_answer)
