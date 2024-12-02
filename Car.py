# Initialize the 'command' variable as an empty string
command = ""

# Variable to track if the car is started or not, initially set to False
started = False

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
            # If not, set 'started' to False and print that the car has stopped
            started = False
            print("Car stopped")

    # If the user enters "help"
    elif command == "help":
        # Print instructions for the available commands
        print("""
start - to start car
stop - to stop car
quit - to quit
              """)

    # If the user enters "quit"
    elif command == "quit":
        # Break the loop to end the program
        break

    # If the user enters something else, print an error message
    else:
        print("I don't understand that...")
