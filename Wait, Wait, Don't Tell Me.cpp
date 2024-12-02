#include <iostream>   // Include the iostream library for input and output operations
#include <string>     // Include the string library to use the string data type

using namespace std;  // Use the standard namespace to simplify code (e.g., no need to write std::cout)

// Function prototypes to declare functions before they are defined
void displayFullLimerick();  // Function to display the complete limerick
void guessLimerick();        // Function to start the guessing game for the limerick
void menu();                 // Function to display the menu and handle user input

int main() {                 // Main function where program execution starts
    menu();                  // Call the menu function to start the program
    return 0;                // Return 0 to indicate successful program completion
}

// Menu function
void menu() {
    while (true) {           // Infinite loop to keep displaying the menu until the user chooses to exit
        // Display the menu options to the user
        cout << "\nMenu:\n";
        cout << "1. Play\n";
        cout << "2. Cheat\n";
        cout << "3. Exit\n";
        cout << "Select an option (1, 2, or 3): ";
        
        int choice;          // Variable to store the user's choice
        cin >> choice;       // Get the user's input and store it in the choice variable

        // Check the user's choice and take the appropriate action
        if (choice == 1) {           // If the user chooses 1, start the guessing game
            guessLimerick();         // Call the guessLimerick function
        } else if (choice == 2) {    // If the user chooses 2, show the complete limerick
            displayFullLimerick();   // Call the displayFullLimerick function
        } else if (choice == 3) {    // If the user chooses 3, exit the program
            cout << "Exiting the game. Goodbye!\n";
            break;                   // Break out of the loop to end the program
        } else {                     // If the user enters an invalid option
            cout << "Invalid option, please try again.\n";
        }
    }
}

// Function to play the guessing game
void guessLimerick() {
    // The limerick with the last word missing
    string limerick = "In pizza tech, changes abound.\n"
                      "The progress they serve is profound.\n"
                      "I'd say it's a miracle to make the box spherical,\n"
                      "a box that is totally...";

    string correctWord = "round";  // The correct missing word that completes the limerick

    // Display the limerick and prompt the user to guess the missing word
    cout << "\nComplete the limerick by guessing the missing word:\n";
    cout << limerick << endl;      // Show the limerick with the missing word
    cout << "(Enter the missing word in all lowercase letters)\n";

    int attempts = 0;              // Counter to track the number of guesses
    const int maxAttempts = 5;     // Constant for the maximum number of attempts allowed
    string guess;                  // Variable to store the user's guess

    // Loop until the user guesses correctly or reaches the maximum number of attempts
    while (attempts < maxAttempts) {
        cout << "Your guess: ";    // Prompt the user to enter a guess
        cin >> guess;              // Store the user's guess in the guess variable

        if (guess == correctWord) {         // Check if the user's guess is correct
            cout << "\nCongratulations!\n"; // Display a success message
            displayFullLimerick();          // Show the complete limerick
            return;                         // End the function if the user guessed correctly
        } else {                            // If the guess is incorrect
            attempts++;                     // Increment the attempts counter
            cout << "Please try again.\n";  // Prompt the user to try again
            int remainingAttempts = maxAttempts - attempts; // Calculate remaining attempts
            if (remainingAttempts > 0) {                    // If the user has attempts left
                cout << "You have " << remainingAttempts << " attempts remaining.\n";
            } else {                      // If the user has used all attempts
                cout << "Game over.\n";   // Display a game over message
                cout << "The correct word was '" << correctWord << "'.\n"; // Show the correct word
            }
        }
    }
}

// Function to display the complete limerick without missing words
void displayFullLimerick() {
    // The full limerick with the missing word included
    string fullLimerick = "In pizza tech, changes abound.\n"
                          "The progress they serve is profound.\n"
                          "I'd say it's a miracle to make the box spherical,\n"
                          "a box that is totally round.";
    cout << "\nFull Limerick:\n" << fullLimerick << endl; // Display the full limerick
}
