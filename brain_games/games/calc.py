import operator
import random

from prompt import string

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

MAX_MULTIPLIER = 30


def generate_round():
    max_num = MAX_MULTIPLIER if '*' in OPERATIONS.keys() else 100
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)

    operation = random.choice(list(OPERATIONS.keys()))

    question = f"{num1} {operation} {num2}"
    correct_answer = str(OPERATIONS[operation](num1, num2))

    return question, correct_answer


def calc_welcome() -> str:
    """Функция приветствия для игры calc."""
    name = ""
    while not name.strip():
        name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


RULE = "What is the result of the expression?"
