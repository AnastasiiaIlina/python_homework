# 1.
# Напишіть лямбда-функцію, яка приймає число і повертає його квадрат.

# result = lambda x: x ** 2

# print(result(3))

# 2. 
# Напишіть лямбда-функцію, яка приймає два аргументи (числа) і повертає їхню суму.
# sum = lambda a,b: a+b

# print(sum(6,4))

# 3.
# Напишіть лямбда-функцію для конвертації температури з градусів Цельсія в градуси Фаренгейта. Використайте цю функцію для конвертації кількох температур.

# 4.
# Напишіть лямбда-функцію для обчислення суми чисел у списку. Створіть список чисел та використайте цю функцію для знаходження їхньої суми.


# 1. 
# Напишіть функцію apply_discount, яка приймає суму покупки та іншу функцію discount_func для обчислення знижки. Функція повинна виводити суму знижки та загальну суму після застосування знижки.

# def discount_func(purchase_sum):
#     if purchase_sum <= 1000:
#         return purchase_sum * 0.1
#     elif purchase_sum <= 5000:
#         return purchase_sum * 0.2
#     else:
#         return purchase_sum * 0.3

# def apply_discount(purchase_sum, discount_func = discount_func):
#     discount_sum = discount_func(purchase_sum)
#     result_sum = purchase_sum - discount_sum

#     print(f'Сума знижки - {discount_sum}')
#     print(f'Сума до сплати - {result_sum}')

#     return result_sum

# apply_discount(1500)

# 2. 
# Напишіть функцію calculator, яка приймає два числа і функцію операції (додавання, віднімання, множення, ділення) і повертає результат цієї операції.


#1. Створіть програму для обробки даних про рейтинг фільмів. Кожен фільм має назву та рейтинг. Напишіть функцію, яка приймає список фільмів та функцію для визначення середнього рейтингу. Використайте цю функцію в лямбді, яка має повертати список фільмів з рейтингом вище середнього.

# films_list = [
#     {
#         'name': "Film1",
#         'rating': 4.4
#     },
#     {
#         'name': "Film2",
#         'rating': 5.0
#     },
#     {
#         'name': "Film3",
#         'rating': 3.5
#     },
#     {
#         'name': "Film4",
#         'rating': 4.7
#     }
# ]

# def calculate_avarage_rating(elements):
#     rating_list = [element['rating'] for element in elements]

#     return sum(rating_list)/len(rating_list)

# result = lambda list,fn: [film['name'] for film in list if film['rating'] > fn(list)]

# print(result(films_list, calculate_avarage_rating))

# 1. Програма для обробки тексту. 
# Напишіть функцію, яка приймає рядок та функцію для перевірки, чи слово починається з певної літери (використовуючи лямбда-функцію). Функція повинна повертати список слів, які відповідають умові.
