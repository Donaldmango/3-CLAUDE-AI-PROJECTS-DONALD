# Donald Nwolisa
# 05/12/2024
# Python Programme for hangman
import random

# List of possible words for the game
words = ['python', 'hangman', 'computer', 'programming', 'developer', 'keyboard', 'challenge']

# Function to choose a random word from the list
def get_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to check if the player has won
def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Main Hangman function
def hangman():
    word = get_word()
    guessed_letters = set()
    attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    
    while attempts < max_attempts:
        print(display_word(word, guessed_letters))

        # Ask for the player's guess
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        # Add the guess to guessed_letters
        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess not in word:
            attempts += 1
            print(f"Incorrect guess. You have {max_attempts - attempts} attempts left.")
        else:
            print(f"Good guess! The letter '{guess}' is in the word.")

        # Check if the player has won
        if check_win(word, guessed_letters):
            print(display_word(word, guessed_letters))
            print("Congratulations! You guessed the word correctly!")
            break
    else:
        print(f"Game Over! The word was '{word}'.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        hangman()

# Start the game
hangman()
