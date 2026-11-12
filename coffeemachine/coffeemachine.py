class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.state = "CHOOSING_ACTION"

    def process_input(self, user_input):
        if self.state == "CHOOSING_ACTION":
            if user_input == "exit":
                return "EXIT"
            elif user_input == "remaining":
                self.print_state()
            elif user_input == "buy":
                self.state = "CHOOSING_BUY"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif user_input == "fill":
                self.state = "FILL_WATER"
                print("Write how many ml of water do you want to add:")
            elif user_input == "take":
                print(f"I gave you {self.money}")
                self.money = 0

        elif self.state == "CHOOSING_BUY":
            if user_input != "back":
                coffee_type = int(user_input)
                req_water, req_milk, req_coffee, cost = 0, 0, 0, 0

                if coffee_type == 1:
                    req_water, req_coffee, cost = 250, 16, 4
                elif coffee_type == 2:
                    req_water, req_milk, req_coffee, cost = 350, 75, 20, 7
                elif coffee_type == 3:
                    req_water, req_milk, req_coffee, cost = 200, 100, 12, 6

                if self.water < req_water:
                    print("Sorry, not enough water!")
                elif self.milk < req_milk:
                    print("Sorry, not enough milk!")
                elif self.coffee < req_coffee:
                    print("Sorry, not enough coffee beans!")
                elif self.cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= req_water
                    self.milk -= req_milk
                    self.coffee -= req_coffee
                    self.cups -= 1
                    self.money += cost

            self.state = "CHOOSING_ACTION"
            self.print_action_prompt()

        elif self.state == "FILL_WATER":
            self.water += int(user_input)
            self.state = "FILL_MILK"
            print("Write how many ml of milk do you want to add:")
        elif self.state == "FILL_MILK":
            self.milk += int(user_input)
            self.state = "FILL_COFFEE"
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "FILL_COFFEE":
            self.coffee += int(user_input)
            self.state = "FILL_CUPS"
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.state == "FILL_CUPS":
            self.cups += int(user_input)
            self.state = "CHOOSING_ACTION"
            self.print_action_prompt()

        return self.state

    def print_state(self):
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def print_action_prompt(self):
        print("Write action (buy, fill, take, remaining, exit):")


def main():
    machine = CoffeeMachine()
    machine.print_action_prompt()

    while True:
        user_input = input("> ")
        result = machine.process_input(user_input)
        if result == "EXIT":
            break
        if machine.state == "CHOOSING_ACTION":
            machine.print_action_prompt()


if __name__ == "__main__":
    main()