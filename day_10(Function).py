"""
def show():  # function without argument
    print("hello")


print("before")
show()  # function calling
print("after")
show()
"""

"""
def add(v, w):  # function definition / formal parameter
    u = v + w
    return u  # function returning value


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = add(a, b)  # function calling / actual parameter
print(c)
"""

# Write a python function to calculate area of rectangle.
"""
def area_rectangle(x, y):
    rectangle_area = 0.5 * (x * y)
    return rectangle_area


h = int(input("Enter the height of rectangle: "))
b = int(input("Enter the base of rectangle: "))
area = area_rectangle(h, b)
print("the area of rectangle is", area)
"""

# Write a python function to calculate the cube of entered number.
"""
def cube(z):
    return z*z*z


num1 = int(input("Enter the number of which you want the cube: "))
cube_num1 = cube(num1)
print("The cube is", cube_num1)
"""

# Write a program to find the greatest element from list of 5 integer values.
list1 = []
count = 1
while count <= 5:
    num2 = int(input("Enter numbers in list: "))
    list1.append(num2)
    count += 1
print(list1)


def maximum(e):
    max1 = 0
    for i in e:
        if max1 < i:
            max1 = i
    return max1


num3 = maximum(list1)

print("The max in list is", num3)
