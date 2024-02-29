# Yes / no / why response function
def string_checker(question, num_letters, valid_responses):

    error = f"Please choose '{valid_responses[0]}' or '{valid_responses[1]}'."

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)
        print()


# Main routine starts here...
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Testing purposes...
for case in range(0, 5):

    see_instructions = string_checker("Do you want to see instructions? ", 1, yes_no_list)

    print(f"Instructions? {see_instructions}")
    print()

for case in range(0, 5):
    payment_method = string_checker("Payment Method: ", 2, payment_list)

    print(f"Payment Method: {payment_method}")
    print()
