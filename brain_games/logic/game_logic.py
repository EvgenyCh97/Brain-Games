import prompt

NUMBER_OF_ROUNDS = 3


def logic(RULES, task, ANSWER_LIST):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES)
    while NUMBER_OF_ROUNDS != 0:
        print(f'Question: {task()}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == ANSWER_LIST[0]:
            print('Correct!')
            NUMBER_OF_ROUNDS -= 1
        else:
            print(f'"{your_answer}" is wrong answer ;(.'
                  f' Correct answer was "{ANSWER_LIST[0]}".'
                  f'\nLet\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
