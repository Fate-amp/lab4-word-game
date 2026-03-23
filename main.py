def update_game_state(secret_word: str,
                     guessed_letters: list[str],
                     guess: str,
                     lives: int) -> tuple[list[str], int]:
    """
    Update guessed letters and remaining lives after a guess in Hangman.
    Args:
        secret_word (str): The word to guess.
        guessed_letters (list[str]): Letters already guessed.
        guess (str): The current guess.
        lives (int): Remaining lives.
    Returns:
        tuple[list[str], int]: Updated guessed letters and lives.
    """
    new_guessed_letters = guessed_letters.copy()
    new_number_of_lives = lives
    # Validate guess: must be a single letter
    if guess.isalpha() and len(guess) == 1:
        # Check if guess is in the word (case-insensitive)
        if guess.lower() in secret_word.lower():
            # Only add if not already guessed (case-insensitive)
            if guess.lower() not in new_guessed_letters:
                new_guessed_letters.append(guess.lower())
        else:
            # Decrement lives for incorrect guess
            new_number_of_lives -= 1

    return new_guessed_letters, new_number_of_lives


def initialize_game(secret_word: str) -> dict:
    """
    Initialize the game state for a new Hangman game.
    Args:
        secret_word (str): The word to guess.
    Returns:
        dict: Game state with guessed_letters, lives, and wrong_letters.
    """
    guessed_letters = []  # Letters guessed so far
    wrong_letters = []    # Incorrect guesses
    return {
        "guessed_letters": guessed_letters,
        "lives": len(secret_word),
        "wrong_letters": wrong_letters
    }

def display_word_state(secret_word: str, guessed_letters: list[str]) -> str:
    """
    Build a string showing guessed letters and masking unknowns with '_'.
    Args:
        secret_word (str): The word to guess.
        guessed_letters (list[str]): Letters already guessed.
    Returns:
        str: Masked word state (e.g. h_ll_).
    """
    word_state = ""
    for letter in secret_word:
        # Reveal letter if guessed, else mask
        if letter in guessed_letters:
            word_state += letter
        else:
            word_state += "_"
    return word_state

def is_won(secret_word: str, guessed_letters: list[str]) -> bool:
    """
    Check if all letters in the secret word have been guessed.
    Args:
        secret_word (str): The word to guess.
        guessed_letters (list[str]): Letters already guessed.
    Returns:
        bool: True if player has won, else False.
    """
    return all(letter in guessed_letters for letter in secret_word)
    

def is_lost(lives: int) -> bool:
    """
    Check if the player has lost (no lives left).
    Args:
        lives (int): Remaining lives.
    Returns:
        bool: True if player has lost, else False.
    """
    return lives == 0

def validate_guess(guess: str) -> bool:
    """
    Validate if the guess is a single alphabetic character.
    Args:
        guess (str): The guessed character.
    Returns:
        bool: True if valid, else False.
    """
    # Check for single alphabetic character
    return guess.isalpha() and len(guess) == 1
