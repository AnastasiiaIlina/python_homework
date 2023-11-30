from functools import wraps

# def uppercase_decorator(func):
#     @wraps(func)
#     def wrapper():
#         return func().upper()
#     return wrapper


# # @uppercase_decorator
# def say_hi():
#     "This will say hi"
#     return 'hello there'

# # print(say_hi())
# print(uppercase_decorator(say_hi)())


# 1. Спробуйте модифікувати попередній приклад, додавши якийсь свій функціонал
def uppercase_decorator(func):
    @wraps(func)
    def wrapper():
        str_result = func()

        return f'Строка {str_result.upper()} має {len(str_result)} кількість символів.' 
    return wrapper


@uppercase_decorator
def say_hi():
    # "This will say hi"
    return 'hello there'

print(say_hi())
# print(uppercase_decorator(say_hi)())

# 2. Напишіть декоратор, який виводить час виконання функції.


# 3. Створіть декоратор, який перевіряє аргументи, передані у функцію, 
# і виводить повідомлення про помилку, якщо аргументи не задовольняють певні умови.