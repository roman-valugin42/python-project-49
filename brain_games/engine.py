from prompt import string

ROUNDS_TO_WIN = 3

def run(game):
    name = welcome_user()
    print(game.RULE)

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = string("Your answer: ").strip().lower()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
  
        print("Correct!")

    print(f"Congratulations, {name}!")

def welcome_user():
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
