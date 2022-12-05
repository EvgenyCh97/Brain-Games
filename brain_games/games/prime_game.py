from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 20


def is_prime(number):
    divisor = 2
    if number == 1:
        return False
    while number % divisor != 0:
        divisor += 1
    if divisor == number:
        return True
    return False


def get_task_and_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(random_number):
        return (str(random_number), 'yes')
    else:
        return (str(random_number), 'no')
