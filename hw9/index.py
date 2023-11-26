# Task 1
# Imports practice
#  Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.

from number_operations import sum
print(sum(5,7))
 

# Task 2
# The sys module.
#  The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.

import sys

# The search path can be manipulated from within a Python program as the variable sys.path.
# For example create folder helpers_for_hw9. There is a module math_operations in this folder. Try to use multiply function from this module.
# We have to change sys.path:

sys.path.append('/Users/ilina/Documents/python_course/helpers_for_hw9')
print(sys.path)

# After that we can successfully use our math_operations module:

import math_operations

print(math_operations.multiply(5,4))
