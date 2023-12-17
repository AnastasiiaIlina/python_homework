# Task 1
# Method overloading.
# Create a base class named Animal with a method called talk 
# and then create two subclasses: Dog and Cat, and make their own 
# implementation of the method talk be different. For instance, 
# Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input 
# instance of a Cat or Dog classes and performs talk method on input parameter.  

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print('Woof!')

class Cat(Animal):
    def talk(self):
        print('Meow!')

def talk(animal):
    return animal.talk()

talk(Dog())
talk(Cat())

# Task 2
# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance 
# of Book class and adds the book to the books list for the current library.

# - group_by_author(author: Author) - returns a list of all books grouped 
# by the specified author

# - group_by_year(year: int) - returns a list of all the books grouped 
# by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.

# Also, the book class should have a class variable which holds 
# the amount of all existing books

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Author(name={self.name}, country={self.country}, birthday={self.birthday})'

    def __str__(self):
        return f'Author name is {self.name}, country - {self.country}, birthday - {self.birthday}.'

class Book:
    books_amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

        Book.books_amount += 1

    def __repr__(self):
        return f'Book(name={self.name}, year={self.year}, author={self.author})'

    def __str__(self):
        return f'Book name is {self.name}, year - {self.year}, author - {self.author}.'

class Library:
    def __init__(self, name):
        self.name = name 
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)

        self.books.append({
            'name': book.name,
            'year': book.year,
            'author': book.author
        })

        return book

    def group_by_author(self, author: Author):
        grouped_books = [book for book in self.books if book['author'].name == author.name]

        return grouped_books
    
    def group_by_year(self, year: int):
        grouped_books = [book for book in self.books if book['year'] == year]

        return grouped_books

    def __repr__(self):
        return f'Library(name={self.name})'

    def __str__(self):
        return f'Library name - {self.name}.'

lib1 = Library('Library 1')

tegmark = Author('Max Tegmark', 'USA', '05.05.1967')
fried = Author('Jason Fried', 'unknown', 'unknown')

lib1.new_book('Our Mathematical Universe', 2014, tegmark)
lib1.new_book('Life 3.0', 2017, tegmark)
lib1.new_book('Rework', 2010, fried)

print(lib1.books)
print(lib1.group_by_author(fried))
print(lib1.group_by_year(2017))
print(Book.books_amount)

# Task 3
# Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну 
# логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок. 
# Потрібно додати магічні методи для математичних операцій та операції порівняння 
# між об'єктами класу Fraction

# GCD - greatest common divisor
def gcd(m, n):
    try:
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n
    except:
        print('Помилка у розрахунках')

        return 1

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, val2):
        new_numerator = self.numerator * val2.denominator + val2.numerator *  self.denominator
        new_denominator = val2.denominator *  self.denominator

        common_gcd = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // common_gcd, new_denominator // common_gcd)
    
    def __sub__(self, val2):
        new_numerator = self.numerator * val2.denominator - val2.numerator *  self.denominator
        new_denominator = val2.denominator *  self.denominator

        common_gcd = gcd(new_numerator, new_denominator)

        return Fraction(new_numerator // common_gcd, new_denominator // common_gcd)
    
    def __mul__(self, val2):
        return Fraction(self.numerator*val2.numerator, self.denominator*val2.denominator)

    def __truediv__(self, val2):
        return Fraction(self.numerator*val2.denominator, self.denominator*val2.numerator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __eq__(self, val2):
        first = self.numerator * val2.denominator
        second = val2.numerator * self.denominator

        return first == second

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    assert x + y == Fraction(3, 4)
    assert x - y == Fraction(1, 4)
    assert x * y == Fraction(1, 8)
    assert x / y == Fraction(2, 1)