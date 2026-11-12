from brain_games.engine import run
from brain_games.games.gcd import RULE, gcd_welcome, generate_round


def main():
    run(RULE, generate_round, gcd_welcome)


if __name__ == "__main__":
    main()
