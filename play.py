from main import (
    update_game_state,
    initialize_game,
    display_word_state,
    is_won,
    is_lost,
    validate_guess,
)
import string
import random

def guess_letter(mode,guessed_letters):
    guess=''
    if mode=='m':
        guess=input("Enter a letter")
    else:
        possible_letters= []
        for letter in string.ascii_lowercase:
            if letter not in guessed_letters:
                possible_letters.append(letter)
        guess=random.choice(possible_letters)
    return guess

def play_game():
    secret_word = "hello"
    game = initialize_game(secret_word)
    mode=input("Enter m for playing or a to start auto play: ")
    while not is_won(secret_word, game["guessed_letters"]) and not is_lost(game["lives"]):
        guess = guess_letter(mode,game["guessed_letters"])
        if validate_guess(guess) and guess not in game["guessed_letters"]:
            new_guessed_letters, new_number_of_lives = update_game_state(
                secret_word, game["guessed_letters"], guess, game["lives"]
            )
            if new_number_of_lives < game["lives"]:
                game["wrong_letters"].append(guess.lower())

            game["guessed_letters"] = new_guessed_letters
            game["lives"] = new_number_of_lives

            print(f"The word:{display_word_state(secret_word, game['guessed_letters'])}")
            print(f"Wrong guesses: {', '.join(game['wrong_letters'])}")
            print(f"Lives left: {game['lives']}")
            print("")
        else:
            print("A valid character is a single letter. Try again")

    if is_won(secret_word, game["guessed_letters"]):
        print("You won!")
    else:
        print("You lost")


replay = "y"
while replay == "y":
    play_game()
    replay = input("Would you like to play again? y/n ").lower()

print("Thanks for playing!")
# play.py: Handles the user interface and game loop for Hangman.
# Imports core logic functions from main.py.
from main import (
    update_game_state,
    initialize_game,
    display_word_state,
    is_won,
    is_lost,
    validate_guess,
)

def play_game():
    """
    Run a single round of Hangman.
    Handles user input, updates game state, and prints progress.
    """
    secret_word = "hello"  # The word to guess (could be randomized)
    game = initialize_game(secret_word)

    # Main game loop: continue until win or loss
    while not is_won(secret_word, game["guessed_letters"]) and not is_lost(game["lives"]):
        guess = input("Enter a letter: ")
        # Validate guess and check for repeats
        if validate_guess(guess) and guess not in game["guessed_letters"]:
            new_guessed_letters, new_number_of_lives = update_game_state(
                secret_word, game["guessed_letters"], guess, game["lives"]
            )
            # If lives decreased, guess was wrong
            if new_number_of_lives < game["lives"]:
                game["wrong_letters"].append(guess.lower())

            # Update game state
            game["guessed_letters"] = new_guessed_letters
            game["lives"] = new_number_of_lives

            # Print current progress
            print(f"The word: {display_word_state(secret_word, game['guessed_letters'])}")
            print(f"Wrong guesses: {', '.join(game['wrong_letters'])}")
            print(f"Lives left: {game['lives']}")
            print("")
        else:
            # Invalid input or repeated guess
            print("A valid character is a single letter. Try again")

    # End of game: print result
    if is_won(secret_word, game["guessed_letters"]):
        print("You won!")
    else:
        print("You lost")

# Replay loop: allows user to play multiple rounds
replay = "y"
while replay == "y":
    play_game()
    replay = input("Would you like to play again? y/n ").lower()

print("Thanks for playing!")

