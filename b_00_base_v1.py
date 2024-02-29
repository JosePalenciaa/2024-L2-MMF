# Functions go here...
import pandas


# Function to check users input
def string_checker(question, valid_list, error, num_letters):
    while True:
        response = input(question).lower()

        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item

        print(error)
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


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # If age is <16, price = $7.50
    if var_age < 16:
        price = 7.50

    # If age is 15 < age < 65, price = $10.50
    elif var_age < 65:
        price = 10.50

    # If age is >64, price = $6.50
    else:
        price = 6.50

    return price


def currency(x):
    return f"${x:.2f}"


# Main routine goes here...

# List(s) go here...
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame i.e: column_lame:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Variables go here...

# Set maximum number of tickets below
MAX_TICKETS = 3

# Tracks # of tickets sold
tickets_sold = 0

# Asks user if they want to see instructions (yes = display, no = continue)
display_instructions = string_checker("Would you like to see Instructions? ", yes_no_list,
                                      "Please enter a valid response (y / n)", 1)

if display_instructions == "yes":
    instructions()

print()

# While there are tickets left to be sold, loop continues
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break

    # Asks the user for their age, if they don't fit the age parameters, return a response
    age = int_checker("Age? ")

    # Age restrictions, will output respective error
    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("Sorry you are to young for this movie.")
        continue

    else:
        print("??? That looks like a typo, please try again.")
        continue

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age} | Ticket Price: {ticket_cost:.2f}")

    # Chooses a payment method
    payment_method = string_checker("Payment Method: ", payment_list,
                                    "Please enter a valid method (ca / cr)", 2)

    # Depending on payment method, there may be a surcharge
    if payment_method == "cash":
        surcharge = 0

    else:
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # Add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)


# Create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index("Name")

# Calculate the total ticket cost (ticket + surcharge_
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# Calculate the profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# Calculate ticket and profit totals
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print(mini_movie_frame)

print()
print("---- Ticket Data ----")

# Output total ticket sales and profit
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")


# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congrats! You have sold all tickets!")

# Says how many tickets have been sold, and how many remaining
else:
    print(f"You have sold {tickets_sold} ticket(s). There is "
          f"{MAX_TICKETS - tickets_sold} ticket(s) remaining.")
