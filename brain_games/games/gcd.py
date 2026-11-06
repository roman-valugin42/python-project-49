import random
from math import gcd

from prompt import string

MIN_NUMBER = 1
MAX_NUMBER = 49


def generate_round():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer


def gcd_welcome() -> str:
    """Функция приветствия для игры gcd."""
    name = ""
    while not name.strip():
        name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


RULE = "Find the greatest common divisor of given numbers."
