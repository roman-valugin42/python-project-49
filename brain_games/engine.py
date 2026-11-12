from prompt import string

ROUNDS_TO_WIN = 3


def default_welcome() -> str:
    """Стандартная функция приветствия."""
    name = ""
    while not name.strip():
        name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run(rule, generate_round, welcome_func):
    name = welcome_func()

    print(rule)

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = generate_round()
        print(f"Question: {question}")

        user_answer = string("Your answer: ").strip().lower()

        if user_answer != correct_answer.lower():
            msg = f"'{user_answer}' is wrong answer ;("
            msg += f". Correct answer was '{correct_answer}'."
            print(msg)
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
