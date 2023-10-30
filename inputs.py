# 1
# Вам потрібно запропонувати замовнику декілька варіантів створення 
# електронних пошт для його працівників. Реалізуйте функціонал 
# генерування пошт (з 3-ма варіантами, 
#  як приклад- taras.shevchenko@kobzar.com, tshev@kobzar.com і тд). 
# * "kobzar.com" - це компанія, для якої ви реалізовуєте цей функціонал. 

# user_name = input('Введіть ваше імʼя: ')
# user_surname = input('Введіть ваше прізвище: ')

# company = 'kobzar.com'

# user_email1 = f'{user_name}@{company}'
# user_email2 = f'{user_name}.{user_surname}@{company}'
# user_email3 = f'{user_surname}@{company}'

# print()
# print(user_email1, user_email2, user_email3, sep='\n')
# print()

# 2. 
# Ви - злий касир в АТБ і продаєте алкогольні напої лише особам старше 18 років. 
# Людям, старше 14 років і молодше 18 років, ви продаєте лише енергетичні напої. 
# Всім решта - будь-що. 
# Напишіть функціонал на пайтоні, який реалізує цей алгоритм.

# user_age = int(input('Введіть ваш вік: '))

# if user_age >=18:
#     print('Alcohol is allowed')
# elif user_age > 14 and user_age < 18:
#     print('Energy drinks are allowed')
# else:
#     print('Nothing is allowed')


# 3. 
# Ви працюєте на проекті, який займається тим, що опрацьовує дані по платежах клієнтів
#  від різних платіжних систем. Дані зберігаються в csv-файлах на Linux сервері. 
# При перекидуванні даних на Windows сервер виявилось, що віндовс додає специфічні 
# символи на позначення початку (";") і закінчення стрічки ("%") з зашифрованим 
# Transaction ID (було "yu7i9om0iymn", стало ";yu7i9om0iymn%"). Це критичний баг для проекту. 
# Реалізуйте механізм на пайтоні, який буде видаляти непотрібні символи з початку і кінця Transaction ID. 

# source = input('Дані з платіжної системи: ')

# if(source[0] == ';'):
#     source = source[1:]

# if(source[-1] == '%'):
#     source = source[:-1]

# print(source)


# 4. 
# Умова та ж сама, але тепер віндовс рандомно додає знак "&" в будь-яку позицію в 
# стрічці Transaction ID (Було "yu7i9om0iymn", стало "yu&7i9om&0iym&n"). 
# Реалізуйте функціонал, який буде видаляти знак "&" зі стрічки.

# source = input('Дані з платіжної системи: ')
# target = source.replace('&', '')

# print(target)

# 1. 
# Створіть програму, яка перевіряє, чи може користувач отримати кредит в банку. 
# Задайте для користувача дані про його дохід, вік та наявність роботи. Врахуйте 
# різні умови, такі як мінімальний дохід, максимальний вік та наявність роботи.

# user_age = int(input('Введіть ваш вік: '))
# user_income = int(input('Введіть суму вашого доходу: '))
# is_user_worked = input('Чи працевлаштовані ви? (y - так, n - ні) ') == 'y'


# if user_age > 65 or user_income <= 7000:
#     print('no credit')
# elif (16000 < user_income <= 50000  and is_user_worked):
#      print('credit')
# elif(user_income > 50000):
#     print('credit')
# else:  
#     print('no credit')


# 2. 
# Напишіть програму, яка перевіряє, чи відповідає користувач вимогам для реєстрації на сайті. 
# Задайте для користувача дані про вік, електронну пошту та пароль. Врахуйте вимоги 
# до віку та складності паролю.

# user_age = int(input('Введіть ваш вік: '))
# user_email = input('Введіть пошту: ')
# user_password = input('Введіть пароль: ')

# isDigitInPassword = False
# isUppercaseLetterInPassword = False

# for c in user_password:
#     if c.isdigit():
#         isDigitInPassword = True

#     if c.upper() == c and c.isalpha():
#         isUppercaseLetterInPassword = True


# is_valid_email = '@' in user_email and '.' in user_email
# is_valid_password = len(user_password) >= 12 and isDigitInPassword and isUppercaseLetterInPassword

# if user_age >= 18 and is_valid_email and is_valid_password:
#     print('valid')
# else:
#      print('invalid')




