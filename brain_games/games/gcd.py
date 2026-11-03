import random
from math import gcd

def generate_round():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer

RULE = "Find the greatest common divisor of given numbers."
