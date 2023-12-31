# Task 1
# School
# Make a class structure in python representing people at school. 
# Make a base class called Person, a class called Student, and another 
# one called Teacher. Try to find as many methods and attributes as you 
# can which belong to different classes, and keep in mind which are 
# common and which are not. For example, the name should be a Person attribute, 
# while salary should only be available to the teacher. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self, phrase):
        return f'{self.name} said: "{phrase}".'
    
    def sleep(self, hours):
        return f'{self.name} sleeps {hours} hours.'


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        self.marks = []

    def print_marks(self):
        print(f'{self.name} has marks: {', '.join(str(x) for x in self.marks)}.')


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def call_the_board(self, student_name):
        print(f'{student_name}, go to the board.')
    
    def give_mark(self, student, mark):
        student.marks.append(mark)

student_ivan = Student('Ivan', 18, '5A')
math_teacther = Teacher('Svitlana', 33, 20000)

math_teacther.call_the_board(student_ivan.name)
math_teacther.give_mark(student_ivan, 11)
math_teacther.give_mark(student_ivan, 8)

student_ivan.print_marks()


# Task 2
# Mathematician
# Implement a class Mathematician which is a helper class for doing math 
# operations on lists.
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
              
class Mathematician:
    def square_nums(self, num_list):
        return [x**2 for x in num_list]

    def remove_positives(self, num_list):
        return [x for x in num_list if x < 0]

    def filter_leaps(self, num_list):
        return [x for x in num_list if not x % 4]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# Task 3
# Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will 
# operate with all products in the store. All methods, in case they can’t 
# perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class. 
# You can also implement additional classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# add(product, amount) - adds a specified quantity of a single product with a predefined 
# price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all 
# products specified by input identifiers (type or name). The discount must be 
# specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from 
# the store if available, in other case raises an error. It also increments income 
# if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and 
# amount of items in the store.


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        self.discount = 0


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        self.products.append({
            'type':product.type, 
            'name': product.name, 
            'price': product.price + product.price * 0.3, 
            'amount': amount,
            'discount': product.discount, 
        })

    # identifier_type = "name" | "type"
    def set_discount(self, identifier, percent, identifier_type='name'):
        is_valid_identifier = False

        for product in self.products:
            if (identifier_type == 'name' and product['name'] == identifier) or (identifier_type == 'type' and product['type'] == identifier):
                is_valid_identifier = True
                product['discount'] = percent

        if not is_valid_identifier:
            raise ValueError('The product with such identifier is not found in store')

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product['name'] == product_name:
                if product['amount'] >= amount:
                    product['amount'] = product['amount'] - amount
                    self.income +=(product['price'] - product['price'] * product['discount'] / 100) * amount
                else:
                    raise ValueError('There is no such product amount in the store')
                   
    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        is_valid_identifier = False

        for product in self.products:
            if product['name'] == product_name:
                is_valid_identifier = True
                return (product_name, product['amount'])
        
        if not is_valid_identifier:
            raise ValueError('The product with such identifier is not found in store')

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Food', 'Sushi', 7)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.add(p3, 250)

s.set_discount('Food', 13, 'type')

s.sell_product('Ramen', 2)
s.sell_product('Football T-Shirt', 5)

print(s.get_income())
print(s.get_all_products())

print(s.get_product_info('Ramen'))


# Task 4
# Custom exception
# Create your custom exception named 'CustomException', you can inherit 
# from base Exception class, but extend its functionality to log every error message 
# to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality for saving
#  messages to file

class CustomException(Exception):
    def __init__(self, msg = 'it`s only for adults!'):
        self.msg = msg
        super().__init__(self.msg)

        with open("logs.txt", "a") as log_file:
            log_file.write(self.msg)
            log_file.write('\n')

age = 14

if age < 18:
    raise CustomException()
   
