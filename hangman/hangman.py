import random


def play_game():
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)

    guessed_letters = set()
    used_guesses = set()
    attempts = 8

    while attempts > 0:
        current_state = "".join([letter if letter in guessed_letters else "-" for letter in word])
        print("\n" + current_state)

        if current_state == word:
            print(f"You guessed the word {word}!")
            print("You survived!")
            return

        guess = input("Input a letter: > ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue

        if not guess.islower() or not guess.isalpha():
            print("Please enter a lowercase English letter")
            continue

        if guess in used_guesses:
            print("You've already guessed this letter")
            continue

        used_guesses.add(guess)

        if guess in word:
            guessed_letters.add(guess)
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1
    else:
        print("You lost!")


def main():
    print("HANGMAN")
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ')
        if choice == "play":
            play_game()
        elif choice == "exit":
            break


if __name__ == "__main__":
    main()