# wap to print the day names as per the user input
"""
day = int(input("Enter a day number\n"))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")
"""

# take a character from user. if it is a, e, i, o, u then print vowel else print consonant.

"""
char = input("Enter an alphabet\n")
if char == 'a':
    print("Vowel")
elif char == 'e':
    print("Vowel")
elif char == 'i':
    print("Vowel")
elif char == 'o':
    print("Vowel")
elif char == 'u':
    print("Vowel")
else:
    print("Consonant")
"""

"""
User will enter two number and user will enter a choice and acc. to user choice perform the following operations:
+ add
- sub
* mul
/ div'
"""

"""
num1 = int(input("Please, enter 1st number\n"))
num2 = int(input("Please, enter 2nd number\n"))
act = input("Enter the choice\n")

if act == '+':
    print("The sum is", num1 + num2)
elif act == '-':
    print("The subtraction is", num1 - num2)
elif act == '*':
    print("The multiplication is", num1 * num2)
elif act == '/':
    print("The division is", num1 / num2)
else:
    print("Invalid Operation")
"""

# Logical Operators

# OR
"""
c = input("Enter a character\n")
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
    print("Vowel")
else:
    print("Consonant")
"""

# Write a program to print weekday if entered day number is 1,2,3,4,5
# and print weekend if entered day is 6 or 7, and invalid day if value not between 1 to 7.
"""
day = int(input("Enter the day number\n"))
if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    print("It is a Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid day")
"""
# Write a program to find greatest among three numbers.

a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
c = int(input("Enter the third number\n"))

if a > b and a > c:
    print(a, "is greatest")
elif b > a and b > c:
    print(b, "is the greatest")
else:
    print(c, "is the greatest")

# A candidate is recruited based on following criteria:
# If male, age should be above 30 yrs and height above 160.
# If female, age should be above 25yrs and height above 155.

gender = input("Enter your gender (Male/Female):\n")
age = int(input("Enter your age:\n"))
height = int(input("Enter your height (in cm)\n"))

if gender == "male" and age > 30 and height > 160:
    print("You are selected")
elif gender == "female" and age > 25 and height > 155:
    print("You are selected")
else:
    print("You don't fit in our criteria")
