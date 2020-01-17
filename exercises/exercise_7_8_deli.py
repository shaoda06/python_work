# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of
# various sandwiches. Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each
# order, such as I made your tuna sandwich. As each sandwich is made, move it
# to the list of finished sandwiches. After all the sandwiches have been
# made, print a message listing each sandwich that was made.

sandwich_orders = ['sandwich 01', 'sandwich 02', 'sandwich 03', 'sandwich 04']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
    print("I made your " + finished_sandwich)

print("Sandwiches I made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
