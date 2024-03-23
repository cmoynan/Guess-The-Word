import random

words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "watermelon", "mango", "melon", "cranberry"]
guessed_words = []

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
    if not words:
        print("\n\033[31mNo words left to choose from. Game over.\033[0m")
        return False  # Return False to indicate the game ends

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
            guess = input("\nGuess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("\n\033[31mError: Please enter only 1 letter and only a letter\033[0m")

        if guess in guessed_letters:
            print("\033[31mYou already guessed that letter!\033[0m")
        elif guess in chosen_word:
            print("\n\033[32mCorrect guess!\033[0m")
            # Add the guessed letter to the set of guessed letters.
            guessed_letters.add(guess)
            if set(guessed_letters) == set(chosen_word):
                # If the set of guessed letters is equal to the set of letters in the chosen word:
                print("\n\033[32mCongratulations! You guessed the word correctly. The word was:", chosen_word, "\033[0m")
                guessed_words.append(chosen_word)
                return True  # Return True to indicate the game ends

        else:
            print("\n\033[31mIncorrect guess!\033[0m")
            attempts -= 1
    
    print("\n\033[31mSorry, you have run out of attempts. The word was:", chosen_word, "\033[0m\n")
    return True  # Return True to indicate the game ends

def main():
    global words
    correct_guesses = 0
    while True:
        if not play_game(words):
            score = len(guessed_words)
            print("\n\033[33mYou guessed", score, "words correctly.\033[0m")
            if not words:
                print("\n\033[33mThanks for playing. We hope to see you again soon\033[0m")
                break
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("\033[33mThanks for playing. We hope to see you again soon\033[0m")
                break
            words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "watermelon", "mango", "melon", "cranberry"]
            guessed_words.clear()

main()  
