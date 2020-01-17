# 8-12. Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich. The function should have one parameter that collects
# as many items as the function call provides, and it should print a summary
# of the sandwich that is being ordered. Call the function three times,
# using a different number of arguments each time.


def make_sandwich(*items):
    """Summarize the sandwiches wre are about to make"""
    print("Making a sandwiches with the following items:")
    for item in items:
        print("-" + item)


make_sandwich("item 1")
make_sandwich("item 1", "item 2")
make_sandwich("item 1", "item 2", "item 3")
