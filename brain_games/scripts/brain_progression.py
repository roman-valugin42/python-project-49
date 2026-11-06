from brain_games.engine import run
from brain_games.games.progression import (
    RULE,
    generate_round,
    progression_welcome,
)


def main():
    run(
        game=type('', (object,), {
            "generate_round": generate_round,
            "RULE": RULE,
            "WELCOME_FUNC": progression_welcome
        })
    )


if __name__ == "__main__":
    main()
