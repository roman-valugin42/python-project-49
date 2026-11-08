from brain_games.engine import make_game, run
from brain_games.games.even import RULE, even_welcome, generate_round


def main():
    game = make_game(RULE, generate_round, even_welcome)
    run(game)


if __name__ == "__main__":
    main()
