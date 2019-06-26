# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary.

# *** Notice that since python 3.6, dict have been changed to ordered.
from collections import OrderedDict

glossary = OrderedDict()

glossary['append'] = '.append()'
glossary['insert'] = '.insert()'
glossary['del'] = 'del '
glossary['remove'] = '.remove'
glossary['pop'] = '.pop()'

for key, value in glossary.items():
    print("Key: " + key)
    print("Value: " + value + "\n")
