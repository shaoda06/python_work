# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

# • Tests for equality and inequality with strings
# • Tests using the lower() function
# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

test_string_0 = "shaoda"
test_string_1 = "Shaoda"

print("Is 'shaoda' == 'Shaoda'? " + str(test_string_0 == test_string_1))
print("Is 'shaoda'.lower() == 'Shaoda'.lower() " + str(
    test_string_0.lower() == test_string_1.lower()))

print("******** Numerical tests ********")
test_num_0 = 25
test_num_1 = 26
print(test_num_0 == test_num_1)
print(test_num_0 > test_num_1)
print(test_num_0 < test_num_1)
print(test_num_0 >= test_num_1)
print(test_num_0 <= test_num_1)

print("******** Multiple conditions and/or ********")
test_predicate_0 = 20
test_predicate_1 = 18
test_answer_0 = 15
test_answer_1 = 18
print(test_predicate_0 == test_answer_0 and test_predicate_1 == test_answer_1)
print(test_predicate_0 == test_answer_0 or test_predicate_1 == test_answer_1)

print("******** Whether or not an item is in a list ********")
test_foods_list = ['apple', 'noodles', 'pizza', 'taco']
test_favorite_food_0 = 'fish'
test_favorite_food_1 = 'hamburger'
print(test_favorite_food_0 in test_foods_list)
print(test_favorite_food_1 not in test_foods_list)
