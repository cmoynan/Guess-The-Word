import random

words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "watermelon", "mango", "melon", "cranberry"]

def choose_word(words):
    """
    Randomly chooses a word from the array to begin the game.
    """
    chosen_word = random.choice(words)
    return chosen_word

def play_game(words):
    """
    Main game function.
    """
    print("Welcome to Guess the Word!")
    print("Try to guess the word within 6 attempts.")
    chosen_word = choose_word(words)

    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        display = "".join(letter if letter in guessed_letters else "_" for letter in chosen_word)
        print("\nWord:", display)
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in chosen_word:
            print("Correct guess!")
            guessed_letters.add(guess)
            if set(guessed_letters) == set(chosen_word):
                print("Congratulations! You guessed the word:", chosen_word)
                return
choose_word(words)
play_game(words)    
