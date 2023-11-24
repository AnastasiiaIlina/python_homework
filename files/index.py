# 1. Читання файлу:

# Створіть текстовий файл example.txt і напишіть в ньому кілька рядків тексту.
# Напишіть програму, яка відкриває цей файл і виводить його вміст на екран.


# with open('example.txt', 'w') as file:
#     file.write('The first line!')

# def print_file_content(file):


# 2. Запис в файл:

# Створіть програму, яка приймає від користувача кілька рядків тексту.
# Запишіть ці рядки у новий текстовий файл output.txt.

# user_input1 = input('Write some text: ') + '\n'
# user_input2 = input('Write some text: ')+ '\n'
# users_inputs = [user_input1, user_input2]

# with open('output.txt', 'a') as file:
#     file.writelines(users_inputs)

# 1. Створіть JSON об'єкт, який представляє інформацію про книгу (назва, автор, рік видання) та збережіть його у файл з ім'ям "book.json".
# Зчитайте інформацію з файлу "book.json" та виведіть на екран у зручному форматі.
# Виведіть кількість книг у списку.



# 2. Створіть CSV файл, який містить інформацію про фрукти (назва, кількість, ціна) для трьох різних фруктів.
# Зчитайте інформацію з файлу CSV та виведіть її на екран.
# Додайте новий рядок інформації про фрукт у існуючий CSV файл.
# Створіть програму, яка обчислює загальну вартість усіх фруктів у файлі та виводить її на екран.

import csv

# fields = []
# rows = []

# with open('fruits.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)

#     fields = next(csvreader)

#     for row in csvreader:
#         rows.append(row)

#     print(rows)

# with open('fruits.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)

#     writer.writerow(fields)

#     rows.append(['груша', 7, 120])
    
#      # writing the fields
#     writer.writerows(rows)

# with open('fruits.csv', 'a') as csvfile:
#     writer = csv.writer(csvfile)

#     writer.writerow(['груша2', 7, 120])
     

# 1. Читання та виведення даних:
# Зчитайте дані з CSV файлу та виведіть перші 5 рядків для ознайомлення.

# 2. Фільтрація та сортування:
# Виведіть список працівників, які проживають в певному місті.

# 3. Статистика:
# Обчисліть середній вік працівників.
# Визначте кількість працівників з кожного відділу.

# 4. Додавання та видалення даних:
# Додайте нового працівника у файл та збережіть зміни.
# Видаліть працівника за певною умовою та оновіть файл.

# with open('nestle_employee.csv', 'a') as csvfile:
#     writer = csv.writer(csvfile)

#     writer.writerow(['Test','Roos','33','+372 98765432','Tallinn','Estonia','Sales','Sales' 'Representative'])

# fields = []
# rows = []

# deleted_number = "+82 9876543211"

# with open('nestle_employee.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)

#     fields = next(csvreader)

#     for row in csvreader:
#         rows.append(row)

#     index = 0
#     for row in rows:
#         if row[3] == deleted_number:
#             break
#         index+=1

#     rows.pop(index)


# with open('nestle_employee.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)

#     writer.writerow(fields)
#     writer.writerows(rows)


# 5. Збереження в новий файл:
# Створіть новий CSV файл та збережіть туди лише певні поля працівників 
# (наприклад, ім'я, вік, відділ).

# 6. Застосування умов:
# Створіть функцію, яка приймає назву відділу та повертає список працівників у цьому відділі.
# def get_employees(department):
#     fields = []
#     rows = []
#     new_rows = []

#     with open('nestle_employee.csv', 'r') as csvfile:
#         csvreader = csv.reader(csvfile)

#         fields = next(csvreader)

#         for row in csvreader:
#             rows.append(row)

#         for employee in rows:
#             if department in employee:
#                 new_rows.append(employee)

#         return new_rows

        

# print(get_employees('IT'))