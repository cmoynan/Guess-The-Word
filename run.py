import random

words = [
    "apple", "banana", "orange", "strawberry", "grape",
    "pineapple", "watermelon", "mango", "melon", "cranberry"
]
guessed_words = []


def choose_word(words):
    """
    Randomly chooses a word from the array to begin the game.
    """
    chosen_word = random.choice(words)

    # Remove the chosen word from the list to prevent repetition
    words.remove(chosen_word)
    return chosen_word


def play_game(words):
    """
    Main game function.
    """
    if not words:
        print("\n\033[31mNo words left to choose from. Game over.\033[0m")
        return False  # Return False to indicate the game ends

    # Display game instructions and hint
    print("\033[33mWelcome to Guess the Word!\033[0m")
    print("Try to guess the word within 6 attempts.")
    print("You only lose an attempt if the attempt is "
          "\033[31mincorrect\033[0m.")
    print("\033[32mThere are 10 words in total to guess from.\033[0m")
    print("\n\033[33mOnce all 10 words are guessed you will be given a "
          "score\033[0m.")

    chosen_word = choose_word(words)

    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        """
manages the main loop of the game. It displays the current state of the word
being guessed and the number of attempts left, and it continues looping until
the player either guesses the word correctly or runs out of attempts
"""
        """
        Display the current state of the word
        being guessed and the number
        of attempts left
        """
        display = "".join(
            letter if letter in guessed_letters else "_"
            for letter in chosen_word)

        display = " ".join(display)
        print("\nWord:", display)
        print("\033[31mAttempts left:\033[0m", attempts)

        # Ask the user to guess a letter
        while True:
            print("\033[33mHint: Each word is a type of fruit\033[0m.")
            guess = input("\nGuess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("\n\033[31mError: Please enter only 1 letter "
                      "and only a letter\033[0m")

        # Check if the guessed letter is already guessed
        if guess in guessed_letters:
            print("\033[31mYou already guessed that letter!\033[0m")
        elif guess in chosen_word:
            print("\n\033[32mCorrect guess!\033[0m")

            # Add the guessed letter to the set of guessed letters.
            guessed_letters.add(guess)

            # Check if all letters of the word have been guessed
            if set(guessed_letters) == set(chosen_word):

                """
                If the set of guessed letters is
                equal to the set of letters
                in the chosen word
                """
                print(
                 "\n\033[32mCongratulations! You guessed the word correctly. "
                 f"The word was: {chosen_word}\033[0m\n")

                guessed_words.append(chosen_word)
                return True  # Return True to indicate the game ends

        else:
            print("\n\033[31mIncorrect guess!\033[0m")
            attempts -= 1

    print(
     "\n\033[31mSorry, you have run out of attempts. "
     f"The word was: {chosen_word}\033[0m\n")

    return True  # Return True to indicate the game ends


def main():

    # Make 'words' accessible globally
    global words
    correct_guesses = 0
    while True:

        # If the game returns False (indicating it's over), exit the loop
        if not play_game(words):

            # Calculate the score by counting the guessed words
            score = len(guessed_words)
            print("\n\033[33mYou guessed", score, "/10 words correct.\033[0m")

            # If there are no more words left to play
            if not words:
                print(
                 "\n\033[33mThanks for playing. "
                 "We hope to see you again soon\033[0m")
                break

            # Prompt the user if they want to play again
            play_again = input("\nDo you want to play again? (y/n): ").lower()

            """
            If the user doesn't want to play again,
            print a farewell message and
            exit the loop
            """
            if play_again != 'y':
                print(
                 "\033[33mThanks for playing. "
                 "We hope to see you again soon\033[0m")
                break

            # Reset the 'words' list and 'guessed_words' list for a new game
            words = [
             "apple", "banana", "orange", "strawberry", "grape",
             "pineapple", "watermelon", "mango", "melon", "cranberry"]

            guessed_words.clear()


main()
