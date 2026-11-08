from brain_games.engine import make_game, run
from brain_games.games.prime import RULE, generate_round, prime_welcome


def main():
    game = make_game(RULE, generate_round, prime_welcome)
    run(game)


if __name__ == "__main__":
    main()
