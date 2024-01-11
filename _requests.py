import requests
import bs4

# 1. Завдання для отримання вмісту веб-сторінки:

# Напишіть програму, яка використовує бібліотеку requests для отримання вмісту веб-сторінки.
# Виведіть заголовок сторінки та перші 100 символів її вмісту.


r = requests.get('https://www.google.com.ua/')

soup = bs4.BeautifulSoup(r.text)
# print(soup.title.text)
# print(soup.getText()[:100])


# 2. Завдання для обробки помилок:

# Напишіть програму, яка відправляє запит до неіснуючого ресурсу (наприклад, неправильний URL).
# Обробіть виняток, який генерується, коли сервер відповідає з помилкою (наприклад, HTTP 404).

try:
    error_response = requests.get('https://www.goooogle.com.ua/')
    print('!!!!!!')
except requests.exceptions.ConnectionError as error:
    print(error)


print('next code')