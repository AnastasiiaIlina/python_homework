# 1. Клас для обчислення площі прямокутника:
# Створіть клас Rectangle, який має атрибути для зберігання 
# довжини та ширини прямокутника. Використовуйте декоратор @property
# для повернення площі прямокутника.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     @property 
#     def get_area(self):
#         return self.length * self.width

# rectangle1 = Rectangle(10, 20)
# print(rectangle1.get_area)

# 2. Створіть дескриптор DiscountLimit, який визначає максимальний обсяг 
# знижки для товару. Забороніть встановлення знижки більше, ніж встановлено за лімітом.

class DiscountLimit:
    def __init__(self, max_discount):
        self.max_discount = max_discount

    def __get__(self, instance, owner):
        return instance._discount
    
    def __set__(self, instance, discount):
        if discount > self.max_discount:
            raise ValueError(f"Discount must be less then {self.max_discount} UAH!")
   
        instance._discount = discount
    
class Good:
    discount = DiscountLimit(200)

good1 = Good()
good1.discount = 40
print(good1.discount)