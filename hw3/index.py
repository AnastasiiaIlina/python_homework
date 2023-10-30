# task1
# The greeting program.
# Make a program that has your name and the current day 
# of the week stored as separate variables and then prints a message like this:
# "Good day <name>! <day> is a perfect day to learn some python."
# Note that  <name> and <day> are predefined variables in source code.
# An additional bonus will be to use different string formatting methods 
# for constructing result string.

name = "Anastasiia"
current_day = "Monday"

print(f"Good day {name}! {current_day} is a perfect day to learn some python.")
print("Good day %s! %s is a perfect day to learn some python." % (name, current_day))
print('Good day {name}! {current_day} is a perfect day to learn some python.'.format(name=name, current_day=current_day))


# Task 2
# Manipulate strings.
# Save your first and last name as separate variables, then use string concatenation 
# to add them together with a white space in between and print a greeting.

first_name = 'Anastasiia'
last_name = 'Ilina'

print(f'Hello {first_name} {last_name}!')
print("Hello " + first_name + " " + last_name + "!")


# Task 3
# Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b, 
# then print the result for each of the following: 
    # Addition
    # Subtraction
    # Division
    # Multiplication
    # Exponent (Power)
    # Modulus
    # Floor division

a = 6
b = 2
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a * b)
print(a ** b)
print(a % b)
print(a // b)