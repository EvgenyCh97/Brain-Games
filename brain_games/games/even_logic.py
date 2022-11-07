import prompt
from random import randint
from brain_games.games.even_calc import is_even_yes_or_no
from brain_games.cli import name_list


def even_game_logic():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 0
    while attempt < 3:
        random_number = randint(1, 20)
        print(f'Question: {random_number}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == is_even_yes_or_no(random_number):
            print('Correct!')
            attempt += 1
        else:
            print(f'"{your_answer}" is wrong answer ;(. Correct answer was "{is_even_yes_or_no(random_number)}".')
            print(f'Let\'s try again, {name_list[0]}!')
            return
    print(f'Congratulations, {name_list[0]}!')