# 1. Створіть клас Person з атрибутами:

# name (public)
# _age (protected)
# __address (private)
# Додайте методи для встановлення та отримання значень атрибутів. Створіть об'єкт цього класу та використовуйте методи для доступу до атрибутів.

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self._age = age
#         self.__address = address

#     def get_address(self):
#         print(self.__address)

#     def set_address(self, address):
#         self.__address = address


# person1 = Person('Petro', 25, 'Lviv')
# person1.get_address()
# person1.set_address('Kyiv')
# person1.get_address()


# 2. Створіть базовий клас Vehicle з атрибутами та методами:

# make (public)
# model (public)
# _year (protected)
# __engine_type (private)
# Створіть підклас Car, який успадковує Vehicle та має свій власний атрибут num_doors. Спробуйте змінити атрибути класів залежно від їх видимості.