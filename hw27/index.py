import multiprocessing

# 1. Багатопроцесорна обробка даних:
# Завдання: Створити програму, яка обробляє великий набір даних, розділяючи обробку на кілька процесів.

# Деталі:
# Завантажте великий набір даних (наприклад, текстовий файл з великою кількістю рядків).
# Розділіть набір даних на рівні частини, кожна з яких буде оброблятися окремим процесом.
# Використовуйте модуль multiprocessing для створення процесів та розподілу частин даних між ними.
# Після обробки кожного фрагмента зберіть результати та об'єднайте їх в один файл або структуру даних.

# generate txt file
# with open('source_file.txt', 'w') as file:
#     for i in range(1000):
#         file.writelines(f'This is task number {i+1}!\n')

def read_file_by_line(line):
    return f'Done: {line}'

if __name__ == '__main__':
    with open('source_file.txt', "r") as source_file:
        source_data = source_file.readlines()

    with multiprocessing.Pool() as pool:
        target_data = pool.map(read_file_by_line, source_data, 4)

    with open('target_file.txt', "w") as target_file:
        target_file.writelines(target_data)

