import random

pencils_count = 0
taken = 0

while True:
    pencils_input = input("How many pencils would you like to use:\n> ")
    if not pencils_input.isdigit():
        print("The number of pencils should be numeric")
        continue
    pencils_count = int(pencils_input)
    if pencils_count <= 0:
        print("The number of pencils should be positive")
        continue
    break

players = ("John", "Jack")
while True:
    current_player = input(f"Who will be the first ({players[0]}, {players[1]}):\n> ")
    if current_player not in players:
        print(f"Choose between '{players[0]}' and '{players[1]}'")
        continue
    break

while pencils_count > 0:
    print("|" * pencils_count)
    print(f"{current_player}'s turn!")

    if current_player == "Jack":
        # Логіка бота
        if pencils_count == 1:
            taken = 1
        elif pencils_count % 4 == 1:
            taken = random.choice([1, 2, 3])
        elif pencils_count % 4 == 0:
            taken = 3
        elif pencils_count % 4 == 3:
            taken = 2
        elif pencils_count % 4 == 2:
            taken = 1
        print(taken)
    else:
        # Хід користувача
        while True:
            taken_input = input("> ")
            if taken_input not in ('1', '2', '3'):
                print("Possible values: '1', '2' or '3'")
                continue
            taken = int(taken_input)
            if taken > pencils_count:
                print("Too many pencils were taken")
                continue
            break

    pencils_count -= taken

    if pencils_count == 0:
        winner = players[1] if current_player == players[0] else players[0]
        print(f"{winner} won!")
        break

    current_player = players[1] if current_player == players[0] else players[0]