import threading
import time

# Створіть список даних (наприклад, список чисел або рядків).
# Розробіть функцію, яка обробляє ці дані (наприклад, сортування, зміна значень тощо).
# Реалізуйте багатопоточну версію функції обробки даних, яка розділить обробку 
# між кількома потоками. Використовуйте модуль threading.

# Виміряйте час виконання обробки даних у багатопоточному та однопоточному режимах.
# Порівняйте результати та зробіть висновки щодо ефективності багатопоточної обробки.

num_list = [num for num in range(1000000)]

def square_numbers(list_):
    return [num**2 for num in list_]

def square_number_with_threads(list_, threads_count):
    threads = []

    chunk_size = len(list_) // threads_count
    chunks = [list_[i: i + chunk_size] for i in range(0, len(list_), chunk_size)]
    
    for chunk in chunks:
        t = threading.Thread(target=square_numbers, args=(chunk,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


sync_start = time.time()
square_numbers(num_list)
sync_end = time.time()

threads_start = time.time()
square_number_with_threads(num_list, 10)
threads_end = time.time()

print(f'Sync mode: {(sync_end - sync_start)* 1000} ms')
print(f'Threads mode: {(threads_end - threads_start)* 1000} ms')

# На швидкість виконання функції впливає кількість 
# потоків, що будуть використані. Задавши 10 потоків для обробки списка з 
# 1 млн елементів можна помітити деяку користь від використання потоків