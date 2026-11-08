from brain_games.engine import make_game, run
from brain_games.games.progression import (
    RULE,
    generate_round,
    progression_welcome,
)


def main():
    game = make_game(RULE, generate_round, progression_welcome)
    run(game)


if __name__ == "__main__":
    main()
