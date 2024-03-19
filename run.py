import random

words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "watermelon", "mango", "melon", "cranberry"]

def choose_word(words):
    """
    Randomly chooses a word from the array to begin the game.
    """
    chosen_word = random.choice(words)
    print("Chosen word:", chosen_word)
    return chosen_word

def play_game(words):
    """
    Main game function.
    """
    print("Welcome to Guess the Word!")
    print("Try to guess the word within 6 attempts.")
    print("test")
    chosen_word = choose_word(words)

choose_word(words)
play_game(words)    
