# Task 1
# Write a function called oops that explicitly raises an IndexError exception 
# when called. Then write another function that calls oops inside a try/except 
# state­ment to catch the error. What happens if you change oops to raise KeyError 
# instead of IndexError?

# Answer: If I change oops to raise KeyError instead of IndexError 
# the program will be crashed

def oops():
    raise IndexError

def handle_error():
    try:
        oops()
    except IndexError:
        print('Such element doesn`t exist!')

handle_error()

# Task 2
# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values 
# given by the input function were not numbers, and if value b was zero 
# (cannot divide by zero).   

def func():
    try:
        a = int(input('Enter a number: '))
        b = int(input('Enter a number: '))

        return a ** 2 / b
    except ValueError:
        return('It`s not a number!')
    except ZeroDivisionError:
        return('We cannot divide by zero!')
  
print(func())