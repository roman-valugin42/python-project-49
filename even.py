# brain_games/even.py
import random

def is_even(number: int) -> bool:
    return number % 2 == 0

def generate_round() -> tuple[str, str]:
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
