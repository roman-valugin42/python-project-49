from brain_games.engine import run
from brain_games.games.prime import generate_round, RULE, prime_welcome

def main():
    run(game=type('', (object,), {"generate_round": generate_round,
                                  "RULE": RULE,
                                  "WELCOME_FUNC": prime_welcome}))

if __name__ == "__main__":
    main()
