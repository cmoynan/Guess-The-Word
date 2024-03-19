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
        """
        manages the main loop of the game. It displays the current state of the 
        word being guessed and the number of attempts left, and it continues looping 
        until the player either guesses the word correctly or runs out of attempts
        """
        display = "".join(letter if letter in guessed_letters else "_" for letter in chosen_word)
        print("\nWord:", display)
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in chosen_word:
            print("Correct guess!")
            # Add the guessed letter to the set of guessed letters.
            guessed_letters.add(guess)
            if set(guessed_letters) == set(chosen_word):
                # If the set of guessed letters is equal to the set of letters in the chosen word:
                print("Congratulations! You guessed the word:", chosen_word)
                return

        else:
            print("Incorrect guess!")
            attempts -= 1

    print("Sorry, you ran out of attempts.Better luck next time. The word was:", chosen_word)               
choose_word(words)
play_game(words)    
