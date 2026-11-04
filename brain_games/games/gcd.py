import random
from math import gcd

MIN_NUMBER = 1
MAX_NUMBER = 49

def generate_round():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer

RULE = "Find the greatest common divisor of given numbers."
