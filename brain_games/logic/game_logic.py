import prompt
from brain_games.cli import name_list


def logic(rules, task, answer_list):
    print(rules)
    attempt = 0
    while attempt < 3:
        print(f'Question: {task()}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == answer_list[0]:
            print('Correct!')
            attempt += 1
        else:
            print(f'"{your_answer}" is wrong answer ;(. Correct answer was "{answer_list[0]}".')
            print(f'Let\'s try again, {name_list[0]}!')
            return
    print(f'Congratulations, {name_list[0]}!')
