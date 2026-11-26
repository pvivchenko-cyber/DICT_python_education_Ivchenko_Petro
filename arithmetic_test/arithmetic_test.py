import random

LEVELS = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29",
}


def choose_level():
    while True:
        print("Which level do you want? Enter a number:")
        print(f"1 - {LEVELS['1']}")
        print(f"2 - {LEVELS['2']}")
        choice = input("> ").strip()
        if choice in LEVELS:
            return choice
        print("Incorrect format.")


def generate_task(level):
    if level == "1":
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(["+", "-", "*"])

        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        else:
            answer = num1 * num2

        return f"{num1} {operator} {num2}", answer

    num = random.randint(11, 29)
    return str(num), num ** 2


def save_result(name, score, level):
    entry = f"{name}: {score}/5 in level {level} ({LEVELS[level]}).\n"
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(entry)
    print('The results are saved in "results.txt".')


def main():
    level = choose_level()
    score = 0

    for _ in range(5):
        question, correct_answer = generate_task(level)
        print(question)

        while True:
            try:
                user_answer = int(input("> "))
                break
            except ValueError:
                print("Wrong format! Try again.")

        if user_answer == correct_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.")
    save_choice = input("> ").strip().lower()

    if save_choice in ("yes", "y"):
        print("What is your name?")
        user_name = input("> ").strip()
        save_result(user_name, score, level)


if __name__ == "__main__":
    main()