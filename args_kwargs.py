# 1. Напишіть функцію, яка приймає будь-яку кількість аргументів та повертає їхню суму.
def get_sum(*numbers):
    return sum(numbers)

print(get_sum(1,2,3,4,5))

# 2. Напишіть функцію, яка приймає будь-яку кількість словників і зливає їх у один.
def merge_dictionaries(*dictionaries):
    merged_dict = {}
    for dictionary in dictionaries:
        merged_dict.update(dictionary)
    return merged_dict

print(merge_dictionaries({'name': 'Nastya'}, {'surname': 'Ilina'}))

# 3. Напишіть функцію, яка приймає ключі та значення (з використанням **kwargs) та повертає словник з цими парами ключ-значення.
def create_dict(**kwargs):
    return kwargs


print(create_dict(name = 'Nastya2', surname = 'Ilina2'))

# 4. Напишіть функцію, яка приймає базову зарплату та додаткові параметри (наприклад, бонуси, виплати за додатковий час тощо) у вигляді **kwargs та розраховує загальну зарплату.

def calculateSalary(**kwargs):
    print(sum(kwargs.values()))

calculateSalary(salary=100, bonus=10, extra=50)

# 5. Напишіть функцію для розсилки електронних повідомлень, яка приймає адресу електронної пошти та додаткові параметри у вигляді **kwargs (тема, текст повідомлення, прикріплення тощо).

def createEmailTemplate(email, **kwargs):
    print(f"Email: {email}.")

    if(kwargs.get('theme')):
        print(f"Тема листа: {kwargs['theme']}.")

    if(kwargs.get('message')):
        print(f"Текст листа: {kwargs['message']}.")
  
# createEmailTemplate('test@gmail.com')
createEmailTemplate('test@gmail.com', message='There is a message')