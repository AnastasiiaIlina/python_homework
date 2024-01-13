import threading
import time
import random

# 1. Створіть дві-три прості функції, які виконують наступні дії:

# Функція 1: Симуляція обробки даних, наприклад, затримка в обробці або обчислення
# (ця функція може "обробляти" велику кількість даних, використовуючи просту затримку. 
#  Наприклад, може просто чекати 2 секунди перед завершенням своєї роботи.)
# Функція 2: Генерація певної інформації або структури даних
# (ця функція може створювати та повертати певну структуру даних, 
#  наприклад, список чи словник з випадковими значеннями.)
# (Опціонально) Функція 3: Інша корисна дія, яка може бути асинхронною або потоковою. 
# (ця функція може представляти будь-який інший корисний процес, наприклад, сортування 
#  списку або конвертацію даних.)

# 2. Реалізуйте ці функції в асинхронному режимі за допомогою asyncio.
# 3. Реалізуйте ці функції в багатопотоковому режимі за допомогою threading.
# 4. Створіть основний скрипт, який демонструє виконання цих функцій в обох режимах.
# 5. Зробіть вимірювання часу виконання для кожної функції в обох режимах.


def proccess_data():
    print("Початок виконання proccess_data...")
    time.sleep(2)
    print("Функція proccess_data завершила виконання!")

def generate_random_list(length = 10000000):
    print("Початок виконання generate_random_list...")
    result = [random.randint(1, 100) for _ in range(length)]

    print("Функція generate_random_list завершила виконання!")
    return result

test_list = [random.randint(1, 100) for _ in range(500000)]
def sort_list(list_=test_list):
    print("Початок виконання sort_list...")
    list_.sort()
    print("Функція sort_list завершила виконання!")
    return list_

def main():
    threads = []
    for _ in range(3):
        thread1 = threading.Thread(target=proccess_data)
        thread2 = threading.Thread(target=generate_random_list)
        thread3 = threading.Thread(target=sort_list)

        thread1.start()  # Запуск потоку 1
        thread2.start()  # Запуск потоку 2 
        thread3.start()  # Запуск потоку 3 
        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)
    
    # Очікуємо завершення всіх потоків
    for thread in threads:
        thread.join()

start = time.time()
main()
end = time.time()

print("The time of execution of above program is :", (end-start), "s")

