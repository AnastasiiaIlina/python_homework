import unittest

# 1. Напишіть функцію, яка приймає два аргументи (числа) і повертає їх суму.

# Тести для функції суми:
# Створіть тест, щоб перевірити, чи правильно функція обробляє невід‘ємні числа.
# Додайте тест для перевірки суми від‘ємних чисел.
# Переконайтесь, що функція правильно обробляє комбінації невід‘ємних та від‘ємних чисел.  

# 2. Напишіть функцію, яка приймає ціле число і перевіряє, чи воно парне.
# Функція повинна повертати True, якщо число парне, і False, якщо непарне.

# Тести для функції перевірки парності:
# Створіть тест для перевірки парного числа.
# Додайте тест для непарного числа.
# Переконайтесь, що функція працює коректно для різних цілих чисел. 

# 3. Напишіть функцію, яка приймає список чисел і повертає найбільше з них.

# Тести для функції знаходження максимуму:
# Створіть тест для перевірки найбільшого числа в списку з невід‘ємних значень.
# Додайте тест для перевірки найменшого числа в списку з від’ємними значеннями.
# Переконайтесь, що функція правильно обробляє найбільший елемент в будь-якому списку.

class MyTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(-4,-5), -9)
        self.assertEqual(sum(-4,5), 1)
        self.assertEqual(sum(4,5), 9)

    def test_even(self):
        self.assertTrue(even(4))
        self.assertTrue(even(0))
        self.assertFalse(even(3))

    def test_max_number(self):
        self.assertEqual(max_number([1,4,7,10]), 10)
        self.assertEqual(max_number([-1,-4,-7,-10]), -1)
        self.assertEqual(max_number([1,-4, 7,-10]), 7)


def sum(a, b):
    return a + b

def even(a):
    return a % 2 == 0

def max_number(numbers):
    return max(numbers)


if __name__ == '__main__':
    unittest.main()


