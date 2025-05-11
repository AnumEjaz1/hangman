import random

words = ['apple', 'banana', 'cherry', 'orange', 'grape']
word = random.choice(words)
guessed_word = ['_'] * len(word)
tries = 6

print("Welcome to Hangman!")

while tries > 0 and '_' in guessed_word:
    print("\nWord: " + ' '.join(guessed_word))
    print(f"Tries left: {tries}")
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        tries -= 1
        print("Wrong guess!")

if '_' not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nSorry, you lost. The word was:", word)
