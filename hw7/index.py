# Task 1
# Make a program that has some sentence (a string) 
# on input and returns a dict containing all unique words 
# as keys and the number of occurrences as values. 

sentence = input('Enter some sentence: ')
words_list = sentence.split(' ')
words_dict = {}

for word in words_list:
    if words_dict.get(word) == None:
        words_dict[word] = words_list.count(word)

print(words_dict)


# Task 2
# Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Compute the total price of the stock where the 
# total price is the sum of the price of an item 
# multiplied by the quantity of this exact item.

# The code has to return the dictionary with the 
# sums of the prices by the goods types.

result_dict = {}
total_price = 0

for product_name in stock:
    if prices.get(product_name):
        result_dict.update({product_name: prices[product_name] * stock[product_name]})


print(f'Total sum of all products is {sum(result_dict.values())} UAH!')

# Task 3
# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j)
# where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

my_list = [(i, i**2) for i in range(1,11)]

print(my_list)

# Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_dict = {}
reverse_day_dict = {}

for key,value in enumerate(days_list, 1):
    days_dict.update({key: value})

for key,value in days_dict.items():
    reverse_day_dict.update({value: key})

print(days_dict)
print(reverse_day_dict)