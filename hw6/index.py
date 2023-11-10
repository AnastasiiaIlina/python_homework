import random

# Task 1
# The greatest number
# Write a Python program to get the largest number 
# from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

random_list = []
i = 0

while i < 10:
    random_int = random.randint(0,9)
    random_list.append(random_int)

    i += 1

print(f'Random list: {random_list}')
print(f'The lasrgest number: {max(random_list)}')

# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random 
# integers from 1 to 10, and make a third list 
# containing the common integers between the 2 initial lists 
# without any duplicates.
# Constraints: use only while loop and random module to generate numbers

first_random_list = []
second_random_list = []
third_random_list = []

list_length = 10
i = 0
k = 0

while i < list_length:
    first_random_int = random.randint(1,10)
    second_random_int = random.randint(1,10)

    first_random_list.append(first_random_int)
    second_random_list.append(second_random_int)

    i += 1


while k < list_length:  
    if first_random_list[k] in second_random_list and (first_random_list[k] in third_random_list) == False:
        third_random_list.append(first_random_list[k])

    if second_random_list[k] in first_random_list and (second_random_list[k] in third_random_list) == False:
        third_random_list.append(second_random_list[k])

    k += 1

print(first_random_list, second_random_list, third_random_list)

# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, 
# then find all integers from the list that are divisible 
# by 7 but not a multiple of 5, and store them in a separate list. 
# Finally, print the list.
# Constraint: use only while loop for iteration

intial_list = []
result_list = []

i = 1
k = 0

while i <= 100:
    intial_list.append(i)
    i += 1

while k < len(intial_list):
    el = intial_list[k]

    if el % 7 == 0 and el % 5 != 0:
        result_list.append(el)

    k += 1

print(result_list)


