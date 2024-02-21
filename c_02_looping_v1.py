# Main routines goes here...

# Set maximum number of tickets below
MAX_TICKETS = 3

# Loop to sell tickets
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congrats! You have sold all tickets!")

else:
    print(f"You have sold {tickets_sold} ticket(s). There is "
          f"{MAX_TICKETS - tickets_sold} ticket(s) remaining.")
