import os

def main():
    # Get the previous number from the disk
    previous_number = get_previous_number()

    # Ask the user to enter a number
    while True:
        try:
            entered_number = int(input("Enter a number: "))
            break
        except ValueError:
            print('Please enter an integer.')

    # Calculate the total number
    total_number = previous_number + entered_number

    # Check if the total number is greater than 152
    if total_number > 152:
        total_number -= 152

    # Display the total number to the user
    print(f"Total number: {total_number}")

    # Save the total number to disk for the next run
    save_total_number(total_number)

def get_previous_number():
    previous_number = 0 # Default value
    if os.path.exists("disk.txt"):
        with open("disk.txt", "r") as file:
            previous_number = int(file.read())
    return previous_number

def save_total_number(total_number):
    with open("disk.txt", "w") as file:
        file.write(str(total_number))
    print("Saved successfully")

if __name__ == "__main__":
    main()