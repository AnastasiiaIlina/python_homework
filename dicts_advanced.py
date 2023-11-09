# 1. Напишіть програму для керування списком книг у бібліотеці. 
# Використовуйте словник (dict) для зберігання інформації про книги, 
# де ключем буде назва книги, а значенням - автор книги. 
# Реалізуйте можливість додавання нових книг, видалення книг і 
# пошуку книг за автором. (тобто користувач повинен мати змогу 
# робити ці всі речі через інпут з терміналу)

# 2. Створіть програму для управління списком клієнтів у компанії. 
# Використовуйте список (list) для зберігання інформації про кожного клієнта, 
# де кожен клієнт представлений словником (dict) з ключами, такими як "ім'я", 
# "посада" і "контактна інформація". Реалізуйте можливість додавання нових 
# клієнтів, видалення клієнтів і пошуку клієнтів за певними критеріями 
# (наприклад, за посадою). (ф-я input() і ввід користувача з терміналу)

# clients = [
#     {
#         'name': 'Maksim',
#         'post': "CEO",
#         'contacts': '+3809454545'  
#     },
#     {
#         'name': 'Anna',
#         'post': "HR manager",
#         'contacts': '+3801111111'  
#     },
#     {
#         'name': 'Vadim',
#         'post': "CTO",
#         'contacts': '+380853331'  
#     }
# ]

# task = input('Enter action - a (ADD), s (SEARCH), d (DELETE): ')

# if task == 'a':
#     name1 = input('Enter client name: ')
#     post1 = input('Enter client post: ')
#     contacts1 = input('Enter client contacts: ')

#     client = {
#         'name': name1,
#         'post': post1,
#         'contacts': contacts1
#     }

#     clients.append(client)

# elif task == 'd' or task == 's':
#     search_string = input('Enter name, post or contacts: ')

#     index = 0

#     for client in clients:
#         for key in client:
#             if client[key] == search_string:
#                 selected_index = index

#                 print(selected_index)
#         index += 1
    
#     if task == 'd':
#         clients.pop(selected_index)
#         print(clients)
#     else:
#         print(clients[selected_index])


# 3. Розробіть програму для керування замовленнями в ресторані. 
# Використовуйте список (list) для зберігання замовлень. Кожне 
# замовлення може містити назву страви, кількість порцій та статус 
# замовлення. Реалізуйте можливість додавання нових замовлень, видалення 
# замовлень, оновлення статусу замовлення та виведення списку активних 
# замовлень. (ф-я input() і ввід користувача з терміналу)

orders = [
    {
        "name": "Salad",
        "amount": 2,
        "status": False #inactive
    },
    {
        "name": "Cake",
        "amount": 1,
        "status": True # active
    },
]

# input1 = input('Enter add, delete, update: ')
# inputName = input('Enter dish name: ')

# if input1 == 'add':
#     inputAmount = int(input('Enter dish amount: '))

#     orders.append({
#         'name': inputName,
#         'amount': inputAmount,
#         'status': True
#     })

# if input1 == 'delete':
#     index = 0

#     for order in orders:
#         if inputName == order['name']:
#             break
#         index+=1

#     orders.pop(index)

# if input1 == 'update':
#     for order in orders:
#         if inputName == order['name']:
#             if order['status']:
#                 order['status'] = False
#             else:
#                 order['status'] = True
#             break

# active_list = list()

# for order in orders:
#         if order['status']:
#             active_list.append(order)

# print(active_list)

# 4. Напишіть програму для управління списком проектів в IT-компанії. 
# Використовуйте кортеж (tuple) для зберігання інформації про кожен проект, 
# наприклад, назву проекту, замовника та строк виконання. 
# Реалізуйте можливість додавання нових проектів, видалення проектів 
# та виведення списку проектів, впорядкованих за строком виконання.
# (ф-я input() і ввід користувача з терміналу)