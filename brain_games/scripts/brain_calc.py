#!/usr/bin/env python3

from ..games import calc_game
from ..game_engine import run_game_engine


def main():
    run_game_engine(calc_game)


if __name__ == '__main__':
    main()
