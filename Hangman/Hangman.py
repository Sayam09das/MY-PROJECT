import random 

words = ['python', 'java', 'c', 'c++', 'javascript', 'go', 'rust']

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\nWord: " + ' '.join(word_display))
    print(f"Remaining attempts: {attempts}")
    
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        print("Good guess!")
    else:
        print(f"'{guess}' is not in the word.")
        attempts -= 1

if '_' not in word_display:
    print("\nCongratulations! You guessed the word:")
    print(' '.join(word_display))
else:
    print("\nGame Over! You've run out of attempts.")
    print(f"The correct word was: {chosen_word}")
