# multiple inheritance
"""
class A:
    a = 100


class B:
    b = 200


class C:
    c = 300


class Total(A, B, C):
    def sum(self):
        print(self.a + self.b + self.c)


t1 = Total()
t1.sum()
"""


#  Data hiding


class Parent:
    __a = 100  # By using "__" before variable in class will hide the data,

    # means that data cannot be accessed outside the class.

    def display(self):
        print(self.__a)


p1 = Parent()
p1.display()  # it will not throw any error because in class functions/methods/functionality can access the hidden data.


# print(p1.__a)  # it will throw an error because "__" variable cannot be accessed outside the class.

# Polymorphism
# ability to take more than one form


class A:
    def __init__(self, a):
        self.a = a

    # adding two objects

    def __add__(self, o):
        return self.a + o.a

    # subtract two objects

    def __sub__(self, o):
        return self.a - o.a

    # multiply two objects

    def __mul__(self, o):
        return self.a * o.a


ob1 = A(1)
ob2 = A(2)
print(ob1 + ob2)
print(ob1 * ob2)
print(ob1 - ob2)
