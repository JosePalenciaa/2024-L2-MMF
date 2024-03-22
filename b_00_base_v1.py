# Functions go here...
import pandas
import random
from datetime import date


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

    print('''\n
***** Instructions *****

For each ticket, enter ...
- The person's name (cannot be blank)
- Their age (between 12 and 120 y/o)
- Desired payment method (cash / credit)

When you have entered all the users, press "xxx" to quit.

The program will then display the ticket details 
including the cost of each ticket, the total cost 
and the total profit.

This information will also be automatically written to a 
text file.

***********************''')


# Function to check user inputs an integer...
def int_checker(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("< Please enter a valid integer >")
            print()


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


# Adds dollar sign...
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
MAX_TICKETS = 5

# Tracks # of tickets sold
tickets_sold = 0

# Asks user if they want to see instructions (yes = display, no = continue)
display_instructions = string_checker("Would you like to see the INSTRUCTIONS? ", yes_no_list,
                                      "Please enter a valid response (y / n)", 1)

if display_instructions == "yes":
    instructions()

# While there are tickets left to be sold, loop continues
while tickets_sold < MAX_TICKETS:
    name = not_blank("\nPlease enter your name or 'xxx' to quit: ")

    if name == "xxx" and len(all_names) > 0:
        break

    elif name == "xxx":
        print("You must sell at least one ticket before quitting!")
        continue

    # Asks the user for their age, if they don't fit the age parameters, return a response
    age = int_checker("Age? ")
    print()

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
    print(f"Name: {name} | Age: {age} | Ticket Price: ${ticket_cost:.2f}")
    print()

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

# Calculate the total ticket cost (ticket + surcharge_
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# Calculate the profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# Calculate ticket and profit totals
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

# Choose a winner from our name list
winner_name = random.choice(all_names)

# Get position of winner name in lift
win_index = all_names.index(winner_name)

# Look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, "Total"]

add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]

for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Set index before printing
mini_movie_frame = mini_movie_frame.set_index("Name")

# Get current date for heading and file name
# Get today's date
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"\n---- Mini Movie Fundraiser Ticket Data ({day} / {month} / {year}) ----\n"
filename = f"MMF_{year}_{month}_{day}"

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = f"Total Ticket Sales: ${total:.2f}"
total_profit = f"Total Profit: ${profit:.2f}"

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The winner of the raffle is {winner_name}. They have won " \
              f"${total_won:.2f}. Their ticket is FREE."

# Heading
print(heading)
print(f"The file name will be {filename}.txt")

print()
print(mini_movie_frame)

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    sales_status = "\n*** All tickets have been sold ***"

# Says how many tickets have been sold, and how many remaining
else:
    sales_status = f"\nYou have sold {tickets_sold} ticket(s). {MAX_TICKETS - tickets_sold} ticket(s) remaining."

to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales,
            total_profit, sales_status, winner_heading, winner_text]

# Print Output
for item in to_write:
    print(item)

# Write output to file
# Create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close the file
text_file.close()
