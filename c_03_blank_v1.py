# Checks that the user's response is not blank
def not_blank(question):
    while True:
        response = input(question).lower()

        if response == "":
            print("Sorry this can't be blank. Plant try again.")

        else:
            return response

# Main routine goes here...


while True:
    ask_name = not_blank("Enter a name (or 'xxx' to quit): ")
    if ask_name == "xxx":
        break

    print("We are done.")
