# Завдання на структури даних в Пайтоні:

# 1. Створіть список (list), що містить ваші улюблені кольори. 
# Виведіть перший і останній елементи списку.

# 2. Створіть кортеж (tuple), який містить назви місяців року. 
# Спробуйте змінити один з елементів кортежу і переконайтеся, що отримаєте помилку.

# 3. Створіть дві множини (set), які містять числа від 1 до 10 
# та від 5 до 15 відповідно. Виведіть їхнє об'єднання, перетин та різницю.

# 4. Створіть список (list), що містить кілька імен і прізвищ. 
# Відсортуйте список за алфавітом і виведіть його відсортований варіант.

# 5. Створіть множину (set), яка містить парні числа від 1 до 20. 
# Створіть ще одну множину, яка містить числа, які діляться на 3. 
# Виведіть об'єднання обох множин.

# set1 = set(range(0,21,2))
# set2 = set(range(3,21,3))

# # i = 1

# # while i <= 20:
# #     if(i%2 ==0):
# #         set1.add(i)
# #     i +=1

# print(set2) 



# 6. Створіть кортеж (tuple), який містить різні типи даних, 
# такі як числа, рядки і булеві значення.

# turple1 = (1, 1.12, 'abc', True)

# 7. Створіть список (list) з чисел і виведіть суму всіх чисел в списку.

# list1 = [1,2,3,4,5]

# sum = 0

# for element in list1:
#     sum+=element

# print(sum)

# 8. Створіть кортеж (tuple), що містить різні предмети 
# (наприклад, фрукти, книги, іграшки). Виведіть п'ятий елемент кортежу.
# turple1 = ('apple', 'banana', 'potatos', 'toy', 'book', 'tomato')

# print(turple1[4])
# print(turple1[-2])

# 9. Створіть список (list) зі словами. Виведіть всі слова, які мають більше 5 літер.

# list1 = ['asd', 'azxc', 'qwerty']

# for element in list1:
#     if len(element)>5:
#         print(element)


# 10. Створити список студентів (кортежів із іменем та середнім балом).
# Знайти студента з найвищим середнім балом та вивести його ім'я.


# 11. Створити список замовлень (кортежів, які містять номер замовлення та суму).
# Знайти загальну суму всіх замовлень і вивести її.
# orders = [(1, 200), (2, 450), (3, 50)]

# sum = 0

# for order in orders:
#     sum += order[1]

# print(sum)

# 12. Створити список кортежів із даними про відвідувачів сайту (IP-адреса та час відвідування).
# Знайти найпопулярніший час доби, коли сайт найбільше відвідують.Реалізуйте функцію 
# для підрахунку загальної кількості відвідувань сайту.Виведіть загальну кількість відвідувань

# users = [('11.11.111.11', '6:30 am'), ('12.12.222.22', '1:00 pm'), ('13.13.333.33', '11:00 pm'), ('14.14.444.44', '04:00pm')]

# am_users_counter = 0
# pm_users_counter = 0

# for user in users:
#     if 'am' in user[1]:
#         am_users_counter+=1
#     else:
#         pm_users_counter+=1

# if am_users_counter > pm_users_counter:
#     popular_time = 'am'
# else:
#      popular_time = 'pm'

# total_users_counter = am_users_counter + pm_users_counter

# print(popular_time, total_users_counter)

# 13. Створити список кортежів, де кожен кортеж містить назву товару та ціну.
# Обчислити загальну вартість товарів з урахуванням податку та вивести її.

# goods = [('pen', 20), ('pencil', 15), ('book', 90)]

# sum = 0

# for good in goods:
#     sum += good[1] + good[1] * 0.2

# print(sum)
# 14. Створити список замовлень, де кожен замовлення - це кортеж, що містить ім'я клієнта, список товарів та їх кількість.
# Розрахувати загальну суму кожного замовлення та вивести її.
# Визначити, які клієнти зробили замовлення на суму більше ніж певне значення і вивести їх імена.