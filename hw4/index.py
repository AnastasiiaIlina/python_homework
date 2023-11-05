# Task 1
# String manipulation
# Write a Python program to get a string made of the first 2 and 
# the last 2 chars from a given string. If the string length is 
# less than 2, return instead of the empty string.

# Sample String: 'helloworld'
# Expected Result : 'held'

# Sample String: 'my'
# Expected Result : 'mymy'

# Sample String: 'x'
# Expected Result: Empty String

# Tips:
# Use built-in function len() on an input string
# Use positive indexing to get the first characters 
# of a string and negative indexing to get the last characters

initial_string = 'helloworld'

first_letters = initial_string[0:2]
last_letters = initial_string[-2:]

if len(initial_string) < 2:
    print('')
else:
    print(first_letters + last_letters)


# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format 
# for a phone number. The program should check that the string 
# contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string 
# evaluation.


tel = '438096593s'

if len(tel) == 10 and tel.isdigit():
    print('Success! Your tel is valid!')
else:
    print('Failed! Your tel is invalid!')


# Task 3
# The math quiz program.
# Write a program that asks the answer for a mathematical expression, 
# checks whether the user is right or wrong, and then responds with 
# a message accordingly.

user_answer = float(input('5 + 5.5 = '))
correct_answer = 10.5

if user_answer == correct_answer:
    print('You are right!')
else:
    print('You are wrong!')

# Task 4
# The name check.
# Write a program that has a variable with your name stored 
# (in lowercase) and then asks for your name as input. The program 
# should check if your input is equal to the stored name even if 
# the given name has another case, e.g., if your input is “Anton” 
# and the stored name is “anton”, it should return True.

name = 'nastya'
input_name = input('Enter your name: ')

if name == input_name.lower():
    print('Name is correct!')
else:
    print('Name is wrong!')