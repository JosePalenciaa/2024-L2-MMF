# Functions go here...
import pandas
import random


# Dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

# Create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index("Name")

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# Calculate the profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# Choose a winner from our name list
winner_name = random.choice(all_names)

# Get position of winner name in lift
win_index = all_names.index(winner_name)

# Look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, "Total"]

# Set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index("Name")
print(mini_movie_frame)

print()
print("---- Raffle Winner ----")
print(f"Congratulations {winner_name}. You have won ${total_won} ie: your ticket is free!")
