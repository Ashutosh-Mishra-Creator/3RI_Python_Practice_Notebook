"""
class Emp:
    def __init__(self, id1, name1):  # parameterized constructor
        self.id = id1
        self.name = name1

    def display(self):
        print(self.id, self.name)


e1 = Emp(101, "Bharti")  # object creation
e2 = Emp(102, "rfg")
e1.display()
e2.display()
"""
"""
class Book:
    def __init__(self, book_id, book_name, book_price):
        self.id = book_id
        self.name = book_name
        self.price = book_price

    def display(self):
        print(self.id, self.name, self.price)


e1 = Book(1, "Life", 120)
e2 = Book(2, "Carrier", 250)
e3 = Book(3, "Religion", 325)
e1.display()
e2.display()
e3.display()
"""

# Write a python program using class which contains two variables of type integer.
# Create and initialize the object using parameterized constructor.
# Write a method to display maximum from given two numbers for all objects.
"""
class num:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def greater(self):
        if self.number1 > self.number2:
            print(self.number1, "is greater")
        else:
            print(self.number2, 'is greater')


e1 = num(17, 27)
e2 = num(25, 37)
e3 = num(67, 57)
e1.greater()
e2.greater()
e3.greater()
"""
# Write a program to perform all the arithmetic operations between two numbers.
"""
class operations:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def addition(self):
        print(self.number1 + self.number2, "is the addition")

    def subtraction(self):
        print(self.number1 - self.number2, "is the subtraction")

    def multiplication(self):
        print(self.number1 * self.number2, "is the multiplication")

    def division(self):
        print(self.number1 / self.number2, "is the division")


e1 = operations(2, 3)
e1.addition()
e1.subtraction()
e1.multiplication()
e1.division()
"""


# Single Inheritance
"""
class Parent:
    surname = "Mishra"


class Child(Parent):
    name = "Ashutosh"

    def show(self):
        print(self.name, self.surname)


c1 = Child()
c1.show()
"""
# multilevel inheritance
class Grandparent:
    middle = "Shyamji"


class Parent:
    surname = "Mishra"


class Child(Parent):
    name = "Ashutosh"

    def show(self):
        print(self.name, self.surname)

