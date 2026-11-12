from brain_games.engine import run
from brain_games.games.prime import RULE, generate_round, prime_welcome


def main():
    run(RULE, generate_round, prime_welcome)


if __name__ == "__main__":
    main()
