from brain_games.engine import run
from brain_games.games.calc import generate_round, RULE, calc_welcome

def main():
    run(
        game=type('', (object,), {
            "generate_round": generate_round,
            "RULE": RULE,
            "WELCOME_FUNC": calc_welcome
        })
    )

if __name__ == "__main__":
    main()
