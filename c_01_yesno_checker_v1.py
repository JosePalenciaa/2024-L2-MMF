# Copy and pasted from previous year...


# Functions go here...
def instructions():

    print("Instructions go here")


def yes_no(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no)")
        print()


# Main routine goes here...

yesno_list = ["yes", "no"]

display_instructions = yes_no("Would you like to see Instructions? ")


# Displays instructions of user says 'yes', loop breaks and continues with rest of code
if display_instructions == "yes":
    print()
    instructions()

# Outputs a statement if user says 'no', loop breaks and continues with rest of code
elif display_instructions == "no":
    print("Alright then. If you say so...")

print("\nprogram continues")
