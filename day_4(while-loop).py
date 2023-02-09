
# wap to print the values from 1 to 10
"""
i = 5  # initialization
while i <= 15:  # condition
    print(i)
    i += 1  # increment
"""

# wap to print values from 20 to 5
"""
count = 20
while count >= 5:
    print(count)
    count -= 1
"""

# Wap a program to print your name 7 times
"""
rep = 1
while rep <= 7:
    print("Ashutosh Mishra")
    rep += 1
"""

# wap to print values from 0 to entered positive no.
"""
i = int(input("Enter a positive no.\n"))
a = 0
while a <= i:
    print(a)
    a += 1
"""

# wap to find the even numbers between 1 and 20
"""
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
"""
# OR

count = 1
while count <= 20:
    if type(count/2) == float:
        print(count)
    count = count + 1

"""
for i in range(11):
    print(i)
for i in range(1, 15):
    print(i)
for i in range(2, 19, 2):
    print(i)
for i in range(20, -1, -2):
    print(i)
"""
# entered name entered number of times using for loop
name = input("Enter your name\n")
num = int(input("How, many times you want to print your name\n"))
for i in range(num):
    print(name)

for i in range(5):
    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))
    print(num+num2)
