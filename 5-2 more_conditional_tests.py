# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

test_string_0 = "shaoda"
test_string_1 = "Shaoda"

print("Is 'shaoda' == 'Shaoda'? " + str(test_string_0 == test_string_1))
print("Is 'shaoda'.lower() == 'Shaoda'.lower() " + str(test_string_0.lower() == test_string_1.lower()))

print("******** Numerical tests ********")
age_shaoda = 25
age_xiaoming = 26
print(age_shaoda == age_xiaoming)
print(age_shaoda > age_xiaoming)
print(age_shaoda < age_xiaoming)
print(age_shaoda >= age_xiaoming)
print(age_shaoda <= age_xiaoming)

print("******** Mutiple conditions and/or ********")
predicate_0 = 20
predicate_1 = 18
answer_0 = 15
answer_1 = 18
print(predicate_0 == answer_0 and predicate_1 == answer_1)
print(predicate_0 == answer_0 or predicate_1 == answer_1)

print("******** Whether or not an item is in a list ********")
foods = ['apple','noodles','pizza','taco']
favorite_food_0 = 'fish'
favorite_food_1 = 'hamburger'
print(favorite_food_0 in foods)
print(favorite_food_1 not in foods)
