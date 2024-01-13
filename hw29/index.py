import asyncio

# Створіть 3 асинхронні функції: task1(), task2(), та task3(). 
# Кожна з цих функцій повинна мати асинхронну затримку, наприклад, за допомогою asyncio.sleep().
# Створіть асинхронну функцію main(), яка викликає ці три функції.
# Запустіть цю основну функцію і спостерігайте порядок виконання задач.

# В коментарях до коду зазначте, в якому порядку викликаються асинхронні задачі.
# Спробуйте різні комбінації виклику функцій в main(), щоб побачити, як змінюється порядок виконання.
# Зверніть увагу на різницю між асинхронним та синхронним виконанням коду.

async def task1():
    print("Початок виконання task1...")
    await asyncio.sleep(1)
    print("Завершення виконання task1...")

async def task2():
    print("Початок виконання task2...")
    await asyncio.sleep(2)
    print("Завершення виконання task2...")

async def task3():
    print("Початок виконання task3...")
    await asyncio.sleep(3)
    print("Завершення виконання task3...")

async def main():
    await asyncio.gather(
        task2(),
        task1(),
        task3()
    )

asyncio.run(main())

# Порядок виконання програми:
# Початок виконання task1...
# Початок виконання task2...
# Початок виконання task3...
# Завершення виконання task1...
# Завершення виконання task2...
# Завершення виконання task3...

# Якщо змінити порядок виклику функцій, то зміниться і порядок початку їх виконання.
# Але порядок їх завершення все одно буде залежати від затримки:

# async def main():
#     await asyncio.gather(
#         task2(),
#         task1(),
#         task3()
#     )

# asyncio.run(main())

# Результат:
# Початок виконання task2...
# Початок виконання task1...
# Початок виконання task3...
# Завершення виконання task1...
# Завершення виконання task2...
# Завершення виконання task3...