# Import necessary module
import random

# Initialize the 'command' variable as an empty string
command = ""

# Variable to track if the car is started or not, initially set to False
started = False

# Variable to track the current gear, initially set to 0 (neutral)
gear = 0

# Maximum speed per gear and top gear
max_speed = 180
gear_speed_increment = 30
top_gear = 6

# Infinite loop to keep the program running until 'quit' command is given
while True:
    # Get user input, convert it to lowercase, and store it in the 'command' variable
    command = input("> ").lower()

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
            # If not, set 'started' to False, reset gear to 0 and print that the car has stopped
            started = False
            gear = 0
            print("Car stopped")

    # If the user enters "shift gear"
    elif command == "shift gear":
        # Check if the car is started
        if not started:
            print("Car is not started. Start the car first.")
        else:
            # Shift to the next gear if it's below the top gear
            if gear < top_gear:
                # Calculate the probability of successful gear shift
                success_probability = 100 - (gear * 50)
                success = random.randint(1, 100) <= success_probability

                if success:
                    gear += 1
                    current_speed = gear * gear_speed_increment
                    print(f"Shifted to gear {gear}. Current speed: {current_speed} km/h")
                else:
                    print("Gear shift failed. Try again.")
            else:
                print("Already in top gear!")

            # Check if the player has reached top gear
            if gear == top_gear:
                print("Congratulations! You have reached gear 6 and won the game!")
                break

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
        break

    # If the user enters something else, print an error message
    else:
        print("I don't understand that...")
