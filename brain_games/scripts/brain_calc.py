#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.calc_game import game


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    game()


if __name__ == '__main__':
    main()
