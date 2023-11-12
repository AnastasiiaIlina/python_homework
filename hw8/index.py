# Task 1
# A simple function.
# Create a simple function called favorite_movie, which takes 
# a string containing the name of your favorite movie. 
# The function should then print "My favorite movie is named {name}".

def favorite_movie(name):
    print(f'My favorite movie is named {name}.')

favorite_movie('Peaky Blinders')

# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name 
# and capital as parameters. Then create a dictionary from those two,
#  with ‘name’ as a key and ‘capital’ as a parameter. Make the function 
# print out the values of the dictionary to make sure that it works as intended. 

countries_dict = {}

def make_country(name, capital): 
    countries_dict[name] = capital
    print(countries_dict)

make_country('Ukraine', 'Kyiv')
make_country('Poland', 'Warszawa')

# Task 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator 
# as a first parameter (to keep things simple let it only be '+', '-' or '*') and 
# an arbitrary number of arguments (only numbers) as the second parameter. Then return 
# the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42  

def make_operation(operator = '+', *numbers):
    if operator == '+':
        return sum(numbers)
    elif operator == '-':
        #expected get at least one number in numbers arg
        return numbers[0] - sum(numbers[1:])
    elif operator == '*':
        multiplication_result = 1
        for number in numbers:
            multiplication_result *=  number

        return multiplication_result
    else:
        return 0
    
print(make_operation('-', 10, 2, 3))
