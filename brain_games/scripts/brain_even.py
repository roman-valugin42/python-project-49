from brain_games.cli import welcome_user
from brain_games.even import generate_round
from prompt import string

ROUNDS_TO_WIN = 3

def main() -> None:
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = string("Your answer: ").strip().lower()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
