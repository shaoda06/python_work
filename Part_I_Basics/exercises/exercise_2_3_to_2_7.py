# 2-3. Personal Message: Store a person’s name in a variable, and print a
# message to that person. Your message should be simple, such as, “Hello
# Eric, would you like to learn some Python today?”
name_2_3 = "Eric"
print("Hello, " + name_2_3 + ", would you like to learn some Python today?")
print(f"Hello, {name_2_3}, would you like to learn some Python today?")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that
# person’s name in lowercase, uppercase, and titlecase.
name_2_4 = "Eric"
print(name_2_4.lower())
print(name_2_4.upper())
print(name_2_4.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”
name_2_5 = "Albert Einstein"
msg = " once said, \"A person who never made a mistake never tried anything " \
      "new.\""
print(name_2_5 + msg)

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous
# person’s name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message. 
name_2_6 = "Albert Einstein"
message_2_6 = name_2_6 + "once said, \"A person who never made a mistake " \
                         "never tried anything new.\" "
print(message_2_6)

# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
name_2_7 = " MrrNonsense "
print("My name is:\n\t" + name_2_7)
name_2_7 = name_2_7.rstrip()
name_2_7 = name_2_7.lstrip()
print("My name is:\n\t" + name_2_7)
