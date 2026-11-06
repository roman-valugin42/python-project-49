import random

from prompt import string

MIN_NUMBER = 1
MAX_NUMBER = 99


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"

    return question, correct_answer


def even_welcome() -> str:
    """Функция приветствия для игры even."""
    name = ""
    while not name.strip():
        name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
