# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # If age is <16, price = $7.50
    if var_age < 16:
        price = 7.50

    # If age is 15 < age < 65, price = $10.50
    elif 15 < var_age < 65:
        price = 10.50

    # If age is >64, price = $6.50
    else:
        price = 6.50

    return price


# Looping for testing...
while True:

    # Get age (assume users input a valid integer)
    age = int(input("Age: "))

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age} | Ticket Price: {ticket_cost:.2f}")
    