# Using continue in a Loop

# Rather than breaking out of a loop entirely without executing the rest of its
# code, you can use the continue statement to return to the beginning of the
# loop based on the result of a conditional test. For example, consider a loop
# that counts from 1 to 10 but prints only the odd numbers in that range:

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
