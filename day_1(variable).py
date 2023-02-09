# Single-line comment

# Multi-line comment
"""print("hello")
print("hi")"""

# Datatypes
"""
a = 10
b = 10.2
c = "Ashutosh"
print(type(a))
print(type(b))
print(type(c))

# Addition of two numbers
print(a + b)
result = a + b
print("result =", result)
"""


# Area of rectangle
"""
l = 5
b = 3
Area = l * b
print("Area of rectangle is =", Area)

# Cube of a number
num = 5
cube = num * num * num
print("Cube of the number given =", cube)
"""

"""
# Taking input from user
a = int(input("Enter the value of first number\n"))
b = int(input("Enter th value of second number \n"))
result = a + b
print("The sum is =", result)
"""
# Enter your details and print the details
print("\n#1")
user = input("Please, enter your name = ")
email = input("Enter your email id = ")
age = int(input("Enter your age = "))
roll_no = int(input("Enter your roll no = "))

print("\nSo, for your confirmation the details you just entered are:")
print("Name:", user, "\nEmail ID:", email, "\nAge:", age, "\nRoll No:", roll_no)

# Write a program to calculate the square of the entered number
print("\n#2")
num = int(input("Please, enter the number for which you want the square\n"))
sq = num*num
print("The square of the number is:", sq)

# Write a program to calculate the avg. of three num
print("\n#3")
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
num3 = int(input("Enter the third number\n"))
avg = (num1 + num2 + num3) / 3
print("Average of the above given number is: ", avg)

a = b = c = 10  # Assign same value to multiple variables
print(a, b, c)
x, y, z = 1, 3, 5  # Assign different values to different variables
print(x, y, z)
