#!/usr/bin/env python3

from brain_games.games.gcd_game import task, RULES
from brain_games.logic.game_logic import logic


def main():
    logic(RULES, task)


if __name__ == '__main__':
    main()
