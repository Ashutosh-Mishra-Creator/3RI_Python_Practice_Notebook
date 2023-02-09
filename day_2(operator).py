"""
# Assignment Operator
a = 10
b = a
print(a, b)
a = 10
a = a + 10
a += 10  # Add and assign # Shorthand
print(a)
b = 5
a += b  # Divide and assign
print(a, b)
"""
"""
# Write a program to decrement the value of entered number by 3
c = int(input("Please Enter a number: "))
c -= 3
print("Your final output after decrement is", c)

# Write a program to swap the values of two integer numbers

# 1
d = 10
temp = c
c = d
d = temp
print(d, c)

# 2
d, c = c, d
print(d, c)

# Comparison/Relational Operator
"""

# Control Statement and it's 3 types:
"""
# 1. Conditional/Decision statement
# 2. Looping/Iterative statement
# 3. Jumping/Branching Statement
"""
"""
# Wap to find the greater between two entered numbers
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))

if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")
  """
"""
# Wap to find two entered number are equal or not
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))

if num1 == num2:
    print("Both are equal")
else:
    print("Both are not equal")
    
# Write a program to find the entered number is positive or negative.
num1 = int(input("Enter the number\n"))

if num1 > 0:
    print(num1, "is positive")
else:
    print(num1, "is negative")

# Wap to find two entered number is even or odd
num1 = int(input("Enter the number\n"))

if num1 % 2 == 0:
    print(num1, "is an even number")
else:
    print(num1, "is an odd number")

# Wap to find the entered character is vowel or not
char = input("Enter the character\n")

if char in [a, e, i, o, u]:
    print(char, "is an vowel")
else:
    print(char, "is a consonant")

# Wap to find the entered number is divisible by 5 or not?
num1 = int(input("Enter the number\n"))

if num1 % 5 == 0:
    print(num1, "is divisible by 5")
else:
    print(num1, "is not divisible by 5")

# Wap to find the entered year is leap year or not?
num1 = int(input("Enter the year\n"))

if num1 % 4 == 0:
    print(num1, "is a leap year")
else:
    print(num1, "is not a leap year")
"""
"""
# Write a program to calculate simple interest taking input from user.
Interest_rate = float(input("Enter the annual interest rate: "))
Principle_amount = int(input("Enter the loan amount: "))
Time_deposited = int(input("Enter the no. of year you want to pay the loan: "))
Simple_interest = (Principle_amount * Interest_rate * Time_deposited) / 100
print("So, the simple interest comes out to be is:\n", Simple_interest)
"""
# Wap to find the entered character is vowel or not
char = input("Enter the character\n")

if char in [a, e, i, o, u]:
    print(char, "is an vowel")
else:
    print(char, "is a consonant")
