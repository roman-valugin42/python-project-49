from brain_games.engine import run
from brain_games.games.calc import RULE, calc_welcome, generate_round


def main():
    run(RULE, generate_round, calc_welcome)


if __name__ == "__main__":
    main()
