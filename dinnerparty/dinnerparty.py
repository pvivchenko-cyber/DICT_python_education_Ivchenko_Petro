import random

num_friends = int(input("Enter the number of friends joining (including you):\n> "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends_dict = {}
    for _ in range(num_friends):
        name = input("> ")
        friends_dict[name] = 0

    total_amount = float(input("Enter the total amount:\n> "))

    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')

    if lucky_choice == "Yes":
        lucky_person = random.choice(list(friends_dict.keys()))
        print(f"{lucky_person} is the lucky one!")

        # Виправляємо потенційну помилку ділення на нуль, якщо учасник всього 1
        if num_friends - 1 == 0:
            split_amount = 0
        else:
            split_amount = round(total_amount / (num_friends - 1), 2)

        for name in friends_dict:
            if name == lucky_person:
                friends_dict[name] = 0
            else:
                friends_dict[name] = split_amount
    else:
        print("No one is going to be lucky")
        split_amount = round(total_amount / num_friends, 2)
        for name in friends_dict:
            friends_dict[name] = split_amount

    print(friends_dict)