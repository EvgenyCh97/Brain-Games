#!/usr/bin/env python3

from brain_games.games.progression_game import task, RULES, ANSWER_LIST
from brain_games.logic.game_logic import logic


def main():
    logic(RULES, task, ANSWER_LIST)


if __name__ == '__main__':
    main()
