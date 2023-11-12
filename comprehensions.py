# Завдання на list, set i dict comprehensions

# 1. Згенеруйте простий список чисел від 1 до 10
print([x for x in range(1,11)])

# 2. Згенеруйте список квадратів чисел від 1 до 10
print([x**2 for x in range(1,11)])

# 3. Згенеруйте список лише з парними числами (початковий список - це послідовність чисел від 1 до 20)
print([x for x in range(1,21) if x%2 == 0])


# 4. Згенеруйте колекцію даних з відфільтрованими унікальними голосними літерами у рядку (тобто вам заздалегідь треба написати якийсь рядок тексту і на основі нього згенерувати нову послідовність)
initial_string = 'abcdifg'

result_string = [x for x in initial_string if x in 'aeiouy']

print(result_string)

# 5. Згенеруйте словник, де ключами є числа від 1 до 5, а значеннями їх квадрати.

ints_dict = {x: x**2 for x in range(1, 6)}

print(ints_dict)

# 6. Створіть словник на основі списку імен, де у value має міститись довжина (кількість букв) імені.
names_list = ['Anastasiia', 'Anna', 'Max']
names_dict = {x: len(x) for x in names_list}

print(names_dict)


# 7. Створіть словник на основі двох списків - з іменами та прізвищами. Ключем може бути ім'я, а значенням - прізвище. Або навпаки:)

names_list = ['Nastya', 'Anna', 'Max']
surname_list = ['Ilina', 'Petrenko', 'Ivanenko']

result_dict = {names_list[x]: surname_list[x] for x in range(len(names_list))}

print(result_dict)

