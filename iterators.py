# class EvenNumbers:
#     max_number = 20

#     def __iter__(self):
#         self.initial = 2
#         return self
    
#     def __next__(self):
#         if self.initial <= self.max_number:
#             x = self.initial
#             self.initial += 2
#             return x
#         else:
#             raise StopIteration


# for x in EvenNumbers():
#     print(x)

# 2. Напишіть генератор паролів, який використовує букви верхнього та нижнього регістрів, цифри та спеціальні символи. Кожен пароль повинен бути різним від попереднього.Також на вхід має передаватись бажана кількість символів (довжина) паролю
import random

def generate_password(length):
    password = random.choices(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ_!'), k = length)

    r(''.join(password))
    # [a-zA-Z]+
    # yield 'a'
    # yield 'b'

generate_password(12)
# for password in generate_password(12):
#     print(password)