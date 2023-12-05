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

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print_info(self):
#         return f'Імʼя - {self.name}. Вік - {self.age} роки.'
    
#     def greet(self):
#         return f'Привіт, {self.name}!'


# ivan = Person('Ivan', 33)
# # print(ivan.print_info())
# print(ivan.greet())


# ======================

# 1. Створіть ієрархію класів для представлення шкільної системи. Почніть з базового класу під назвою Person, який включає такі атрибути, як ім'я та вік. Створіть підкласи для студента та викладача, які успадковують від Person. Кожен підклас повинен мати додаткові атрибути та методи, специфічні для їх ролі. Тестуйте свої класи, створюючи екземпляри студентів і викладачів і отримуючи доступ до їхніх атрибутів і методів.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    


# 2. Створіть ієрархію класів для представлення різних типів транспортних засобів. Почніть з базового класу під назвою Vehicle і додайте такі атрибути, як марка, модель і рік. Створіть підкласи для певних типів транспортних засобів, таких як автомобіль, мотоцикл і вантажівка. Кожен підклас повинен мати додаткові атрибути та методи, специфічні для типу автомобіля. Тестуйте свої класи, створюючи екземпляри різних транспортних засобів і отримуючи доступ до їхніх атрибутів і методів.

# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def get_info(self, name):
#         return f'{name} {self.brand} {self.model}'


# class Car(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)

#     def get_info(self):
#         return super().get_info('Car')
    

# car1 = Car('Toyota', 'Camry', 2020)

# class Motorcycle(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)

#         self.places = 2

#     def get_places(self):
#         return f'Motorcycle has {self.places} sit places'

# motorcycle1 = Motorcycle('mot_brand', 'mot_model', 2009)
# print(motorcycle1.get_places())

# class Truck(Vehicle):
#     max_weight = 4000

#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)

#     def check_weight(self, weight):
#         if weight > self.max_weight:
#             return f'Вага {weight} перевищує допустиму!'
#         else:
#             return f'Вага {weight} є допустимою.'

# truck1 = Truck('truck_brand', 'truck_model', 2011)

# print(truck1.check_weight(5000))
    

# 3. Створіть ієрархію класів для представлення системи управління запасами онлайн-магазину. Почніть з базового класу під назвою Product і додайте такі атрибути, як назва, ціна та кількість. Створюйте підкласи для певних типів товарів, таких як електроніка, одяг і книги. Кожен підклас повинен мати додаткові атрибути та методи, специфічні для типу продукту. Створіть методи додавання нових продуктів, оновлення кількості та розрахунку загальної вартості запасів.


# 4. Ієрархія співробітників компанії
# Побудуйте ієрархію класів для представлення працівників компанії. Включіть такі класи, як:

# Співробітник: базовий клас із такими атрибутами, як ім'я, посада та зарплата.
# Керівник: успадковується від класу Співробітник з додатковими атрибутами, як-от кількість підлеглих. Додайте метод розрахунку загальної заробітної плати з урахуванням премії за кількістю підлеглих.

# Розробник: успадковується від класу Співробітник. Додайте метод розрахунку оцінки продуктивності на основі кількості завершених проектів.

# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self, name, salary, staff_amount):
#         super().__init__(name, 'manager', salary)

#         self.staff_amount = staff_amount

#     def calculate_salary(self):
#         if self.staff_amount > 50:
#             return self.salary + self.salary*0.5
#         elif self.staff_amount > 25:
#             return self.salary + self.salary*0.25
#         else:
#             return self.salary + self.salary*0.1

# class Developer(Employee):
#     desired_projects_amount = 5
#     def __init__(self, name, salary):
#         super().__init__(name, "developer", salary)

#     def calculate_kpi(self, projects_amount):
#         return projects_amount/self.desired_projects_amount * 100
    
# manager1 = Manager('Ivan', 30000, 51)
# print(manager1.calculate_salary())

# dev1 = Developer('Petro', 50000)
# print(dev1.calculate_kpi(2))

