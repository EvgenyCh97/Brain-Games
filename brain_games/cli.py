import prompt


name_list = []


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    name_list.append(name)
