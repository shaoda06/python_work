# • Admission for anyone under age 4 is free.
# • Admission for anyone between the ages of 4 and 18 is $5.
# • Admission for anyone age 18 or older is $10.
# • Admission for anyone 65 or older is $5.

age = 12
if age < 4:
    print("Your admission cost is: $0.")
elif age < 18:
    print("Your admission cost is: $5.")
elif age < 65:
    print("Your admission cost is: $10.")
else:
    print("Your admission cost is: $5.")

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is: $" + str(price) + ".")

if age < 4:
    price = 0
elif age > 18 and age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is: $" + str(price) + ".")

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is: $" + str(price) + ".")
