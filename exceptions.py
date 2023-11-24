# 1. Напишіть програму, яка приймає два числа від користувача і виводить результат ділення першого числа на друге. Оберіть такі числа, щоб викликати помилку ділення на нуль і використайте блок try-except для відловлення цієї помилки та виведення відповідного повідомлення.

# def getDivisionResult(num1, num2):
#     try:
#         result = num1 / num2
#         return result
#     except ZeroDivisionError:
#         return 'На нуль ділити не можна!'

# print(getDivisionResult(5,2))

# 2. Запитайте користувача ввести число у вигляді рядка. Використайте блок try-except, щоб перевірити, чи введено коректне число, і виведіть повідомлення про помилку у протилежному випадку.

# string_number = input('Enter some number: ')

# try:
#     number = float(string_number)
#     print('Your number is right!')
# except ValueError:
#     print('Your number is wrong!')

# 3. Спробуйте отримати доступ до елементу списку за індексом, який перевищує розмір списку. Використайте блок try-except, щоб відловити виняток і вивести повідомлення про помилку.
my_list = [1,2,3,4,5]

try:
    result = my_list[10]
    print(f'10-й елемент у списку - {result}')
except IndexError:
    print(f'Такого елементу не існує')

# 4. (optional) Напишіть функцію, яка приймає два аргументи і виконує ділення першого на друге. Використайте блок try-except, щоб вивести повідомлення про помилку, якщо дільник рівний нулю

# зроблено у першому завданні


# 5. (optional) Запитайте користувача ввести своє ім'я та вік. Використайте блок try-except, щоб перевірити правильність введення даних та вивести повідомлення про помилку за необхідності.

user_name = input('Enter your name: ')
user_age = input('Enter your age: ')


try:
    user_age_int = int(user_age)

    if len(user_name) <= 2:
        raise NameError

except ValueError:
    print('Некоректний вік!')
except NameError:
    print('Імʼя занадто коротке')
