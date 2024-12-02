import random  

name = input("What's your name? ")
print("Good luck,", name, "!")  # Display a welcome message

# Function to load words from a file
def load_words(filename): 
    with open(filename, "r") as file:
        words = file.read().splitlines()  
    return words  # Return the list of words

# Function to choose a random word from the word list
def choose_random_word(word_list):
    return random.choice(word_list)  # Use random.choice to pick a word randomly

# Load the word list from the file
word_list = load_words("/Users/mainuser/python/guessing/word_list.txt")

# Choose a random word from the loaded list
random_word = choose_random_word(word_list)

print("Guess the characters!")  # Prompt the user to guess the word

# Initialize variables
guesses = ''  
turns = 12  

# Main game loop
while turns > 0:
    failed = 0  

    for char in random_word:  # Iterate over each character in the random word
        if char in guesses:  # Check if the character has been guessed
            print(char, end="")  # If guessed, display the character
        else:
            print("_", end="")  # If not guessed, display an underscore
            failed += 1  # Increment the failed counter for every missing character

    print() 

    # Check if the user has guessed all the characters
    if failed == 0:
        print("You Win!")  # If no characters are left to guess, the user wins
        print("The word is:", random_word)  
        break 

    # Ask the user to guess a character
    guess = input("Guess a character: ")
    guesses += guess  # Add the guessed character to the guesses list

    # Check if the guessed character is in the random word
    if guess not in random_word:
        turns -= 1  # Reduce the number of turns by 1
        print("Wrong!")  
        print("You have", turns, "more guesses!")  

        # If no turns are left, the user loses
        if turns == 0:
            print("You Lose!")  # Reveal the correct word

