import random

words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "watermelon", "mango", "melon", "cranberry"]

def choose_word(words):
    """
    Randomly chooses a word from the array to begin the game.
    """
    chosen_word = random.choice(words)
    words.remove(chosen_word)
    return chosen_word
  
def play_game(words):
    """
    Main game function.
    """

    print("\n\033[33mWelcome to Guess the Word!\033[0m")
    print("\nTry to guess the word within 6 attempts.")
    print("You only lose an attempt if the attempt is \033[31mincorrect\033[0m")
    print("\n\033[33mHint: Each word is a type of fruit\033[0m")

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

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("\n\033[31mError: Please enter only 1 letter and only a letter\033[0m")

        if guess in guessed_letters:
            print("\n\033[31mYou already guessed that letter!\033[0m")
        elif guess in chosen_word:
            print("\n\n\033[32mCorrect guess!\033[0m")
            # Add the guessed letter to the set of guessed letters.
            guessed_letters.add(guess)
            if set(guessed_letters) == set(chosen_word):
                # If the set of guessed letters is equal to the set of letters in the chosen word:
                print("\033[32m\nCongratulations! You guess the word correctly. The word was:", chosen_word, "\033[0m")
                return

        else:
            print("\n\033[31mIncorrect guess!\033[0m")
            attempts -= 1
    
    if not restart_game():
        return
        
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
            print("\nInvalid input. Please enter 'y' to play again or 'n' to quit.")   
                     

choose_word(words)
play_game(words)
restart_game()    
