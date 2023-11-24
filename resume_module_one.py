# 1. 
# У вас є дані по покупкам, здійсненим у вашому онлайн-магазині. Вам потрібно реалізувати функціонал, який надасть базову статистику по здійсненим покупкам. Надайте дані по наступним моментах:
# - Які 3 продукти ваші клієнти купують найчастіше?
# - Які 3 продукти ваші клієнти купують найрідше?
# - Скільки разів клієнти купували кожен з ваших продуктів?

orders_data = ['Banana', 'Apple', 'Tomato','Potatoes', 'Cucumber', 'Apple',  'Apple',  'Apple', 'Tomato', 'Cucumber']
orders_stats = dict()

for order in orders_data:
    if order in orders_stats:
        orders_stats[order] += 1
    else:
        orders_stats[order] = 1

def last(n):
    return n[1]

orders_tuples = [(k, v) for k, v in orders_stats.items()]


def print_max_demand_products(products_tuple):
    max_demand_products = sorted(products_tuple, key=last)[-3:]
    print('Клієнти найчастіше купують: ')

    for product in max_demand_products:
        print(f'Продукт {product[0]} був куплений {product[1]} разів')

def print_min_demand_products(products_tuple):
    min_demand_products = sorted(products_tuple, key=last)[:3]
    print('Клієнти найрідше купують: ')

    for product in min_demand_products:
        print(f'Продукт {product[0]} був куплений {product[1]} разів')

print_max_demand_products(orders_tuples)
print_min_demand_products(orders_tuples)



# 2. 
# Напишіть програму для управління розкладом занять в навчальному закладі. Використовуйте словник (dict) для зберігання розкладу. Ключем буде день тижня, а значенням - список предметів на цей день. Реалізуйте можливість додавання нових занять, видалення занять та виведення розкладу на певний день. (ф-я input() і ввід користувача з терміналу)

# 3. 
# Створіть список чисел від 1 до 10 за допомогою list comprehension.
# Створіть множину квадратів чисел від 1 до 10 за допомогою set comprehension.
# Створіть словник, де ключами будуть числа від 1 до 5, а значеннями їх квадрати, за допомогою dict comprehension.

# 4. 
# Використовуючи цикл while, зчитуйте числа з користувача до тих пір, поки він не введе 0.

# 5. 
# Створіть функцію, яка обчислює середнє арифметичне зі списку чисел.

# 6.
# Напишіть функцію, яка відкриває файл і повертає його вміст. Обробіть винятки, якщо файл не існує.