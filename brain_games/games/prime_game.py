from random import randint
from brain_games.logic.game_logic import logic

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
answer_list = ['']
numbers_list = list(range(1, 21))


def task():
    random_number_from_list = randint(0, len(numbers_list) - 1)
    number = numbers_list[random_number_from_list]
    devisor = 2
    if number == 1:
        answer_list[0] = 'no'
        numbers_list.pop(random_number_from_list)
        return number
    while number % devisor != 0:
        devisor += 1
    if devisor == number:
        numbers_list.pop(random_number_from_list)
        answer_list[0] = 'yes'
        return number
    numbers_list.pop(random_number_from_list)
    answer_list[0] = 'no'
    return number


def game():
    logic(rules, task, answer_list)
