from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ANSWER_LIST = ['']
NUMBERS_LIST = list(range(1, 21))


def task():
    random_number_index = randint(0, len(NUMBERS_LIST) - 1)
    random_number = NUMBERS_LIST[random_number_index]
    divisor = 2
    if random_number == 1:
        ANSWER_LIST[0] = 'no'
        NUMBERS_LIST.pop(random_number_index)
        return random_number
    while random_number % divisor != 0:
        divisor += 1
    if divisor == random_number:
        NUMBERS_LIST.pop(random_number_index)
        ANSWER_LIST[0] = 'yes'
        return random_number
    NUMBERS_LIST.pop(random_number_index)
    ANSWER_LIST[0] = 'no'
    return random_number
