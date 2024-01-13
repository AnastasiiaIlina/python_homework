import time
import random
import asyncio

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


async def proccess_data():
    print("Початок виконання proccess_data...")
    await asyncio.sleep(2)
    print("Функція proccess_data завершила виконання!")

async def generate_random_list(length = 10000000):
    print("Початок виконання generate_random_list...")
    async def coroutine_fn(length):
        return [random.randint(1, 100) for _ in range(length)]

    result = await coroutine_fn(length)

    print("Функція generate_random_list завершила виконання!")
    return result

test_list = [random.randint(1, 100) for _ in range(500000)]
async def sort_list(list_=test_list):
    print("Початок виконання sort_list...")

    async def sort_fn():
        list_.copy()

    await sort_fn()

    print("Функція sort_list завершила виконання!")
    return list_

async def main():
    await asyncio.gather(
        sort_list(),
        proccess_data(),
        generate_random_list()
    )

start = time.time()
asyncio.run(main())
end = time.time()

print("The time of execution of above program is :", (end-start), "s")

