#!/usr/bin/env python3

from brain_games.games.progression_game import rules, task, answer_list
from brain_games.logic.game_logic import logic


def main():
    logic(rules, task, answer_list)


if __name__ == '__main__':
    main()
