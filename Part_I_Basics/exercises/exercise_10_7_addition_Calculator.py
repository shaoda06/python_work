# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

prompts = "Please enter two numbers, and I will add them together.\n" \
          "Enter 'quit' to stop."
while True:
    first_number = input("First number: ")
    if first_number == 'quit':
        break

    second_number = input("Second number: ")
    if second_number == 'quit':
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("You can only enter intergers.")
    else:
        sum = first_number + second_number
        print(
            str(first_number) +
            " + " +
            str(second_number) +
            " = " +
            str(sum))
