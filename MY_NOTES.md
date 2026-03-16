<!-- My original thinking -->
**What are the states of a game like Hangman?**
I've identified 5 states:
1.NotStarted: to track when the game starts
2.InProgress: to track the progress of the game 
3.Won: When the failed attempts limit is not reached and teh user manages to guess the secret word
4.Lost: When the number of failed attempts reaches the length of the secret word
5.Invalid input: When the user enters something invalid, like a letter that's not in the word or a special character

**What variables are required?**
1.game_state to track the, well, game's state :)
2.secret_word to keep track of the word
3.guessed_letters to keep track of the letters users has guessed
4.word_state to keep track of the state of the correct guesses
5.wrong_letters for the wrong ones
6.failed_attempts because we need it for the lost state
7.max_attempts, again for the lost state

**What are the rules and invariants?**
1.failed attempts cannot exceed max_attempts
2.Only letters are allowed, no spaces or special characters
3.The state should only be changed to won if the words match exactly

**What kind of bugs and edge cases should we be careful about?**
1.Repeated letters in the secret word: guessing the letter once should reveal all its positions in word_state, but only add it once to guessed_letters.
2.Empty input, special characters, or multiple letters: prompt the user again without changing the game state.
3.All input letters are converted to lowercase before checking, so the game is case-insensitive.


<!-- CoPilot Suggestions -->
<!-- Please note: I first gathered a set of answers to all the four questions above based on what CoPilot was asking me, then asked for its specific suggestion:
Here are my suggestions for each of the four questions in your file: -->

1. **States of a Hangman game:**  
   - NotStarted: Before the first guess.
   - InProgress: User is actively guessing.
   - Won: All unique letters in the secret word have been guessed.
   - Lost: User has reached the maximum number of failed attempts.
   - InvalidInput: User entered an invalid guess (e.g., not a single letter).

2. **Variables required:**  
   - game_state: Tracks the current state.
   - secret_word: The word to guess.
   - guessed_letters: Set or list of all guessed letters.
   - word_state: Representation of the word with correct guesses revealed.
   - wrong_letters: List of incorrect guesses.
   - failed_attempts: Number of incorrect guesses.
   - max_attempts: Maximum allowed failed attempts (often len(secret_word)).

3. **Rules and invariants:**  
   - Only single alphabetic characters are accepted as guesses.
   - No duplicate guesses in guessed_letters or wrong_letters.
   - failed_attempts ≤ max_attempts at all times.
   - The game ends with Won if all unique letters are guessed, or Lost if failed_attempts == max_attempts.
   - word_state always accurately reflects the current progress.

4. **Bugs and edge cases:**  
   - Repeated guesses (should not penalize or should warn the user).
   - Case sensitivity (normalize input to lowercase).
   - Secret word with repeated letters (all positions should be revealed).
   - Empty, multi-character, or special character input (should prompt again).
   - Secret word containing non-alphabetic characters (should be sanitized or rejected).


   <!-- Auto play observations -->
   I had to find where to implement a function for the guess functionality, which was the main challenge. The rest, implementing the function where it used the random library or asked the user for the input, was fairly straightforward.
   
   Question: One thing that must be imporved is the fact that I'm creating an array each time the guess_letter is called, but I'm not sure on how to handle that problem
   Also I'm not really sure it works for edge cases