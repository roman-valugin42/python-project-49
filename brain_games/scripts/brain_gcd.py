from brain_games.engine import run
from brain_games.games.gcd import generate_round, RULE

def main():
    run(game=type('', (object,), {"generate_round": generate_round, "RULE": RULE}))

if __name__ == "__main__":
    main()
