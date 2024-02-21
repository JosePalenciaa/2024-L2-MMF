# Functions go here...

# Function to check users input
def yes_no(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no)")
        print()


# Function to check the user does not input blanks
def not_blank(question):
    while True:
        response = input(question).lower()

        if response == "":
            print("Sorry this can't be blank. Plant try again.")
            print()

        else:
            return response


# Function to output instructions
def instructions():

    print("Instructions go here")


# Function to check user inputs an integer...
def int_checker(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a valid integer")


# Main routine goes here...

# List(s) go here...
yesno_list = ["yes", "no"]

# Variables go here...

# Set maximum number of tickets below
MAX_TICKETS = 3

# Tracks # of tickets sold
tickets_sold = 0

# Asks user if they want to see instructions (yes = display, no = continue)
display_instructions = yes_no("Would you like to see Instructions? ")

if display_instructions == "yes":
    instructions()

print()

# While there are tickets left to be sold, loop continues
while tickets_sold < MAX_TICKETS:
    ask_name = not_blank("Please enter your name or 'xxx' to quit: ")

    if ask_name == "xxx":
        break

    # Asks the user for their age, if they don't fit the age parameters, return a response
    age = int_checker("Age? ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("Sorry you are to young for this movie.")
        continue

    else:
        print("??? That looks like a typo, please try again.")
        continue

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congrats! You have sold all tickets!")

else:
    print(f"You have sold {tickets_sold} ticket(s). There is "
          f"{MAX_TICKETS - tickets_sold} ticket(s) remaining.")
