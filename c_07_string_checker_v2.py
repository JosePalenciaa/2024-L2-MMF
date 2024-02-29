# Yes / no / why response function
def string_checker(question, valid_list, error, num_letters):
    while True:
        response = input(question).lower()

        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item

        print(error)
        print()


yesno_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Testing purposes...
for case in range(0, 5):

    see_instructions = string_checker("Do you want to see instructions? ", yesno_list,
                                      "Please enter a valid response (y / n)", 1)

    print(f"Instructions? {see_instructions}")
    print()

for case in range(0, 5):
    payment_method = string_checker("Payment Method: ", payment_list,
                                    "Please enter a valid method (ca / cr)", 2)

    print(f"Payment Method: {payment_method}")
    print()
