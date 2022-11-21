import prompt
NUMBER_OF_ROUNDS = 3


def logic(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.RULES)
    round = NUMBER_OF_ROUNDS
    while round != 0:
        (question, correct_answer) = game_module.get_task_and_answer()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == correct_answer:
            print('Correct!')
            round -= 1
        else:
            print(f'"{your_answer}" is wrong answer ;(.'
                  f' Correct answer was "{correct_answer}".'
                  f'\nLet\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
