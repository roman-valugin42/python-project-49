from prompt import string

def welcome_user() -> str:
    name = ''
    while not name.strip():
        name = string("May I have your name? ")
    
    print(f"Hello, {name}!")
    return name
