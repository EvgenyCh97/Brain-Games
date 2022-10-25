from random import randint


random_number = randint(1, 20)


def is_even(random_number):
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'
