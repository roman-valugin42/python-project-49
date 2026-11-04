import random

MIN_NUMBER = 1
MAX_NUMBER = 99

def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"

    return question, correct_answer

RULE = "Answer 'yes' if the number is even, otherwise answer 'no'."
