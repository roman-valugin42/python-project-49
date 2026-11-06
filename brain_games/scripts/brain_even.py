from brain_games.engine import run
from brain_games.games.even import generate_round, RULE, even_welcome

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
