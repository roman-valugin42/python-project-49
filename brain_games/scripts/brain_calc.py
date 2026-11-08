from brain_games.engine import make_game, run
from brain_games.games.calc import RULE, calc_welcome, generate_round


def main():
    game = make_game(RULE, generate_round, calc_welcome)
    run(game)


if __name__ == "__main__":
    main()
