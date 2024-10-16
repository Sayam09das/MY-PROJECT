# Hangman Game

This is a simple command-line version of the Hangman game, where the player tries to guess a randomly chosen programming language word, letter by letter. The player has 8 attempts to guess the word before the game ends.

## How to Play

1. Run the Python script.
2. A random word from a list of programming languages will be chosen.
3. The player guesses letters one by one.
4. For every correct guess, the letter is revealed in the word.
5. For incorrect guesses, the number of attempts decreases.
6. The game ends when:
   - The player guesses the entire word (win).
   - The player runs out of attempts (lose).

## Example Gameplay

```bash
Welcome to Hangman!

Word: _ _ _ _ _ _ _ _ _ _ 
Remaining attempts: 8
Guess a letter: p
Good guess!

Word: p _ _ _ _ _ _ _ _ _ 
Remaining attempts: 8
Guess a letter: z
'z' is not in the word.

Word: p _ _ _ _ _ _ _ _ _ 
Remaining attempts: 7
Guess a letter: y
Good guess!

Word: p y _ _ _ _ _ _ _ _ 
Remaining attempts: 7
...
