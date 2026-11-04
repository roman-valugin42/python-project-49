import random

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
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

RULE = "What is the result of the expression?"
