import random

MIN_START = 1
MAX_START = 50
MIN_STEP = -7
MAX_STEP = 7

def generate_progression(start=None, step=None):
    length = random.randint(5, 10)

    start = start or random.randint(MIN_START, MAX_START)
    while True:
        step = step or random.randint(MIN_STEP, MAX_STEP)
        if step != 0:
            break

    progression = [start + i * step for i in range(length)]
    return progression


def generate_round():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)

    question_list = [
        ".." if index == hidden_index else str(num)
        for index, num in enumerate(progression)
    ]
    question = " ".join(question_list)

    correct_answer = str(progression[hidden_index])

    return question, correct_answer

RULE = "What number is missing in the progression?"
