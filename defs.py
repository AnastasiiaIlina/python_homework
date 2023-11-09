# 1. Напишіть функцію, яка приймає два аргументи (числа) і повертає їх суму.

# def sum(a,b):
#     return a + b

# print(sum(5,6))


# 2. Напишіть функцію, яка приймає ціле число і перевіряє, чи воно парне. 
# Функція повинна повертати True, якщо число парне, і False, якщо непарне.

# def isEven(integer):
#     if integer % 2 == 0:
#         return True
#     else:
#         return False

# print(isEven(21))

# 3. Напишіть функцію, яка приймає список чисел і повертає найбільше з них.

# def getMaxNumber(*numbers):
#     max_number = numbers[0]
#     for number in list(numbers):
#         if number >  max_number:
#             max_number = number
#     return max_number


# def getMaxNumber(list_numbers):
#     max_number = list_numbers[0]
#     for number in list_numbers:
#         if number >  max_number:
#             max_number = number
#     return max_number
    
# print(getMaxNumber([1,9, 2,3]))