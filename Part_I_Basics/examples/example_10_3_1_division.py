# 10.3.1 Handling the ZeroDivisionError Exception
# print(5 / 0)

# 10.3.2 Using try-except block
try:
    print(5 / 0)
except BaseException:
    print("You can not divide by zero!")

# 10.3.3 Using Exceptions to Prevent Crashes
# 10.3.4 The else Block
print("Give me two number, and I will divide them. (Integer only!)")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide by 0!")
    except ValueError:
        print("You can only enter integers!")
    else:
        print(answer)
