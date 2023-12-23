# 1. Клас для обчислення площі прямокутника:
# Створіть клас Rectangle, який має атрибути для зберігання 
# довжини та ширини прямокутника. Використовуйте декоратор @property
# для повернення площі прямокутника.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property 
    def get_area(self):
        return self.length * self.width

rectangle1 = Rectangle(10, 20)
print(rectangle1.get_area)

# 2. Створіть дескриптор DiscountLimit, який визначає максимальний обсяг 
# знижки для товару. Забороніть встановлення знижки більше, ніж встановлено за лімітом.