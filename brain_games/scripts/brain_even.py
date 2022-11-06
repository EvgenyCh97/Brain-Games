#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.even_logic import even_game_logic


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    even_game_logic()


if __name__ == '__main__':
    main()
