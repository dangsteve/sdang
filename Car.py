# Import necessary module
import random  # Import the 'random' module to generate random numbers for gear shift success

# Initialize the 'command' variable as an empty string
command = ""  # This variable will store the user's input command

# Variable to track if the car is started or not, initially set to False
started = False  # Tracks whether the car is currently started or not

# Variable to track the current gear, initially set to 0 (neutral)
gear = 0  # Keeps track of the current gear of the car, starts at 0 (neutral)

# Maximum speed per gear and top gear
max_speed = 180  # Maximum speed the car can achieve
gear_speed_increment = 30  # Speed increment per gear
top_gear = 6  # The highest gear the car can reach

# Variable to track the success increase per successful shift
success_increase = 0  # Increases the likelihood of a successful gear shift each time a shift is successful

# Variable to track the number of breaks or failed shifts
fail_count = 0  # Counts the number of times the user fails to shift gear or stops the car
max_fail_count = 10  # Maximum number of fails allowed before the game ends

# Variable to track the probability increase when stopping the car
stop_increase = 50  # Initial increase in success probability after stopping

# Infinite loop to keep the program running until 'quit' command is given
while True:
    # Get user input, convert it to lowercase, and store it in the 'command' variable
    command = input("> ").lower()  # Get input from the user and convert it to lowercase to avoid case issues

    # If the user enters "start"
    if command == "start":
        # Check if the car is already started
        if started:
            # If it is, print that it's already started
            print("Car already started")
        else:
            # If not, set 'started' to True and print that the car has started
            started = True
            print("Car started...Ready to go!")

    # If the user enters "stop"
    elif command == "stop":
        # Check if the car is already stopped
        if not started:
            # If it is, print that it's already stopped
            print("Car is already stopped")
        else:
            # If not, set 'started' to False, reset gear to 1 and print that the car has stopped
            started = False  # Set 'started' to False to indicate the car is stopped
            gear = 1  # Reset gear to 1 when the car is stopped
            success_increase += stop_increase  # Increase success probability by stop increase value
            stop_increase *= 0.75  # Reduce stop increase value by 25% for the next stop
            fail_count += 1  # Increment the fail count since the car was stopped
            print("Car stopped, returning to gear 1.")

            # Check if the player has failed too many times
            if fail_count >= max_fail_count:
                print("You have failed too many times. You are in last place.")
                break  # End the game if the fail count exceeds the limit

    # If the user enters "shift gear"
    elif command == "shift gear":
        # Check if the car is started
        if not started:
            print("Car is not started. Start the car first.")
        else:
            # Shift to the next gear if it's below the top gear
            if gear < top_gear:
                # Calculate the probability of successful gear shift
                success_probability = 100 - (gear * 50) + success_increase  # Calculate the chance of successfully shifting gear
                success_probability = min(success_probability, 100)  # Cap the probability at 100%
                success = random.randint(1, 100) <= success_probability  # Determine if the shift is successful

                if success:
                    gear += 1  # Increment the gear if the shift is successful
                    success_increase += 5  # Increase the chance of success for future shifts
                    current_speed = gear * gear_speed_increment  # Calculate the current speed based on the gear
                    print(f"Shifted to gear {gear}. Current speed: {current_speed} km/h")
                else:
                    fail_count += 1  # Increment the fail count if the shift fails
                    success_increase += 25  # Increase success probability by 25% after each failed shift
                    print("Gear shift failed. Try again.")

                    # Check if the player has failed too many times
                    if fail_count >= max_fail_count:
                        print("You have failed too many times. You are in last place.")
                        break  # End the game if the fail count exceeds the limit
            else:
                print("Already in top gear!")

            # Check if the player has reached top gear
            if gear == top_gear:
                if fail_count == 0:
                    print("Congratulations! You have reached gear 6 and won the game in first place!")
                else:
                    print(f"Congratulations! You have reached gear 6 and finished in place {fail_count + 1}!")
                break  # End the game once the player reaches the top gear

    # If the user enters "help"
    elif command == "help":
        # Print instructions for the available commands
        print("""
start - to start car
stop - to stop car
shift gear - to shift to the next gear
help - to display this help message
quit - to quit
              """)

    # If the user enters "quit"
    elif command == "quit":
        # Break the loop to end the program
        break  # Exit the game

    # If the user enters something else, print an error message
    else:
        print("I don't understand that...")  # Print an error message for unrecognized commands

