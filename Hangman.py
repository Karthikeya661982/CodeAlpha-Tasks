import random

# Predefined list of words
words = ["python", "apple", "tiger", "house", "music"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display hidden word
display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        print("✅ Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!")
        incorrect_guesses += 1

# End of game
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)