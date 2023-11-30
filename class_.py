# 1. Створіть клас Car, який має атрибути brand, model і year. 
# Також, створіть об'єкт(інстанс/екземпляр) цього класу та виведіть 
# інформацію про цей автомобіль.
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def print_info(self):
#         return f'Автомобіль {self.brand} {self.model}. {self.year} року випуску.'

# toyota = Car('Toyota', 'Camry', 2020)
# print(toyota.print_info())



# 2. Розширте клас Car з попереднього завдання, додавши метод start(), 
# який виводить повідомлення про те, що автомобіль почав рухатися.

# 3. Клас "Книга":
# Створіть клас Book, який має атрибути title, author та year. Напишіть метод для виведення інформації про книгу.

# 4. Створіть клас Person, який має атрибути ім'я та вік. Створіть об'єкт цього класу та виведіть інформацію про цю особу.


# 5. Розширте клас Person з попереднього завдання, додавши метод вітатися, який буде виводити привітання з ім'ям особи. (для того, щоб вивести ім'я особи, ви можете використати поле self.name в методі. Достатньо буде просто передати self як параметр, а всередині через self звернутись до атрибутів класу Person)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        return f'Імʼя - {self.name}. Вік - {self.age} роки.'
    
    def greet(self):
        return f'Привіт, {self.name}!'


ivan = Person('Ivan', 33)
# print(ivan.print_info())
print(ivan.greet())