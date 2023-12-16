# 1. Створіть класи Author та Book. Клас Book має включати інформацію про книгу (назва, рік випуску тощо) та об'єкт класу Author як її автора.


# 2. Створіть класи Grade та Student. Клас Student має включати об'єкт класу Grade для представлення його оцінок.

# class Grade:
#     def __init__(self, grades):
#         self.grades = grades
    
#     def print_(self):
#         for grade in self.grades:
#             print(f'Студент отримав {grade} балів')

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = Grade(grades)


# student1 = Student('Ivan', [10,11,10])
# student1.grades.print_()

# 3. Створіть класи Order та User. Клас Order має включати інформацію про замовлення 
# та об'єкт класу User як його власника.

# 1. Створіть класи Bank, Account та Customer. Клас Bank повинен містити список облікових записів (Account), а клас Customer - список облікових записів користувача.

# 2. Створіть класи School, Classroom та Student. Клас School має включати список класів (Classroom), а клас Classroom - список учнів (Student).

# class School:
#     classrooms = []

#     def add_classroom(self, classroom):
#         self.classrooms.append(classroom)

#         return self.classrooms


# class Classroom:
#     students = []

#     def add_student(self, student):
#         self.students.append(student)

#         return self.students
        

# class Student:
#     def __init__(self, name):
#         self.name = name

# 3.Створіть класи Restaurant, Menu, Dish та Order. Клас Restaurant 
# має включати список меню (Menu), а Menu - список страв (Dish). 
# Замовлення (Order) може містити різні страви (Dish).

# class Restaurant:
#     menus = []

#     def add_menu(self, menu, name):
#         self.menus.append({'name': name, 'list': menu.dishes})

# class Menu:
#     def __init__(self):
#         self.dishes = []

#     def add_dish(self, dish):
#         self.dishes.append({'name': dish.name, 'price': dish.price})

# class Order:
#     def __init__(self):
#         self.dishes = []

#     def add_dish(self, dish):
#         self.dishes.append(dish)

#     def get_price(self):
#         total_price = 0

#         for dish in self.dishes:
#             total_price += dish.price

#         return f'Your order price - {total_price} UAH'


# class Dish:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# salad = Dish('Salad', 70)
# potatoes = Dish('Potatoes', 50)

# menu1 = Menu()
# menu1.add_dish(salad)
# menu1.add_dish(potatoes)

# res1 = Restaurant()
# res1.add_menu(menu1, 'Vegan')

# new_order = Order()
# new_order.add_dish(salad)
# new_order.add_dish(salad)
# new_order.add_dish(potatoes)

# print(new_order.get_price())

# 1. Створіть клас Temperature, який має внутрішню змінну для зберігання температури у градусах Цельсія. Використовуйте дескриптор для перетворення температури у градуси Фаренгейта при зверненні до атрибуту.

# print(temp1.temp)

# 2. Створіть клас Circle, який має радіус. Використовуйте @property для повернення площі круга.
# 3. Створіть дескриптор CartLimit, який визначає максимальну кількість продуктів у кошику користувача. Забороніть додавання більше продуктів, ніж встановлено за лімітом.

class CartLimit:
    def __init__(self):

    def __get__()