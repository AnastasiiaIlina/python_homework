# 1. Напишіть свій власний модуль для операцій над рядками, який містить функції для об'єднання рядків, обрізання пробілів і т.д. Потім використайте цей модуль у вашому основному файлі.
import str_operations
from num_operations import get_sum, get_subtract

# print(str_operations.merge_strings('a', 'b'))
# print(str_operations.strip_spaces('   a   '))

# 2. Створіть власний модуль для виконання математичних операцій, таких як додавання, віднімання і т. д. Використайте цей модуль у програмі для розрахунку суми та різниці двох чисел.
print(get_sum(4,5))
print(get_subtract(3,2))

# 3. (optional) Спробуйте винести в окремі файли вже раніше написані вами функції і імпортувати їх в іншому файлі, також зробивши виклик з потрібними аргументами для тих функцій