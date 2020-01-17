# Using break to Exit a Loop
prompt = "Please enter the name of a city you have visited: "
prompt += "\nEnter 'quit' when you are finished."
while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")
    # If 'quit' have been input, the message bellow will not be printed.
    print("Something here!")
