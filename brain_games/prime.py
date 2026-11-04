import random
from prompt import string

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    
    return question, correct_answer


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True


def prime_welcome():  
    name = ''
    while not name.strip():
        name = string("May I have your name? ")
    
    print(f"Hello, {name}!")
    return name


RULE = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
