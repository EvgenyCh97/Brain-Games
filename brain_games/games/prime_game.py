from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 20


def is_prime(number):
    divisor = 2
    if number == 1:
        return (number, 'no')
    while number % divisor != 0:
        divisor += 1
    if divisor == number:
        return (number, 'yes')
    return (number, 'no')


def get_task_and_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    return is_prime(random_number)
