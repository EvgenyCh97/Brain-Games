from random import randint

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
answer_list = ['']
numbers_list = list(range(1, 21))


def task():
    random_number_index = randint(0, len(numbers_list) - 1)
    random_number = numbers_list[random_number_index]
    devisor = 2
    if random_number == 1:
        answer_list[0] = 'no'
        numbers_list.pop(random_number_index)
        return random_number
    while random_number % devisor != 0:
        devisor += 1
    if devisor == random_number:
        numbers_list.pop(random_number_index)
        answer_list[0] = 'yes'
        return random_number
    numbers_list.pop(random_number_index)
    answer_list[0] = 'no'
    return random_number
