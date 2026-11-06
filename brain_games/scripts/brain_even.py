from brain_games.engine import run
from brain_games.games.even import RULE, even_welcome, generate_round


def main():
    run(
        game=type('', (object,), {
            "generate_round": generate_round,
            "RULE": RULE,
            "WELCOME_FUNC": even_welcome
        })
    )


if __name__ == "__main__":
    main()
