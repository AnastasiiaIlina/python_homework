# Завдання для циклу for:

# 1. Виведіть всі непарні числа в інтервалі від 1 до 20 за допомогою циклу for.

# 2. Створіть список чисел та знайдіть суму всіх елементів у списку за допомогою циклу for.

# 3. Створіть список слів і виведіть слова, які містять більше ніж 5 літер, за допомогою циклу for.

# 4. Створіть список, який містить числа від 1 до 10. Виведіть всі числа, 
# крім числа 3, за допомогою циклу for.

# 5. Створіть список з різних типів даних (числа, рядки, булеві значення) і виведіть 
# тип кожного елемента за допомогою циклу for.

# Завдання для циклу while:

# 1. Використовуючи цикл while, виведіть всі парні числа в інтервалі від 1 до 20.

# i = 1

# while i <= 20:
#     if(i%2):
#         print(i)
#     i+=1


# 2. Створіть змінну "сума" і додавайте до неї числа від 1 до 10 
# за допомогою циклу while. Виведіть отриману суму.

# i = 1
# sum = 0

# while i <=10:
#     sum +=i
#     i+=1

# print(sum)

# 3. Створіть змінну "лічильник" (counter) та використовуйте цикл while,
#  щоб підрахувати кількість чисел, які діляться на 5 в інтервалі від 1 до 100.

# i = 1
# counter = 0

# while i <= 100:
#     if(i%5 == 0):
#         counter+=1
#     i+=1
# print(counter)

# 4. Запитайте користувача про пароль. Використовуйте цикл while, 
# щоб продовжувати запитувати пароль, поки він не введе правильний пароль.

# correct_password = 'qwerty1234'
# user_password = input('Введіть пароль: ')

# while 

# 5. Створіть список чисел та виведіть його елементи з використанням циклу while.

list_numbers = [1,2,3,4,5]

i = 0

while i < len(list_numbers):
    print(list_numbers[i])
    i+=1