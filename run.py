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
        display = " ".join(display)
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
                print("\nCongratulations! You guess the word correctly. The word was:", chosen_word)
                return

        else:
            print("Incorrect guess!")
            attempts -= 1
    
    if not restart_game():
        
  

def restart_game():
    """
    Asks the player if they want to play again and returns True if yes, False otherwise.
    """
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == 'y':
            play_game(words)
        elif play_again == 'n':
            print("\nThanks for playing. We hope to see you again soon")
            return
        else:
            print("Invalid input. Please enter 'y' to play again or 'n' to quit.")    

choose_word(words)
play_game(words)
restart_game()    
