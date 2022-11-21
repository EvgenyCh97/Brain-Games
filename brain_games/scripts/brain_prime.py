#!/usr/bin/env python3

import brain_games.games.prime_game
from brain_games.logic.game_logic import run_game_engine


def main():
    run_game_engine(brain_games.games.prime_game)


if __name__ == '__main__':
    main()
