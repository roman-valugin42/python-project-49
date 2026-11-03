import random

def generate_progression(start: int = None, step: int = None) -> list[int]:
    length = random.randint(5, 10)
    if start is None:
        start = random.randint(-20, 20)
    if step is None:
        while True:
            step = random.randint(-9, 9)
            if step != 0:
                break

    return [start + i * step for i in range(length)]

def generate_round() -> tuple[str, str]:
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
