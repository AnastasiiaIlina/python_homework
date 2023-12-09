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

class School:
    classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

        return self.classrooms


class Classroom:
    students = []

    def add_student(self, student):
        self.students.append(student)

        return self.students
        

class Student:
    def __init__(self, name):

# 3.Створіть класи Restaurant, Menu, Dish та Order. Клас Restaurant має включати список меню (Menu), а Menu - список страв (Dish). Замовлення (Order) може містити різні страви (Dish).