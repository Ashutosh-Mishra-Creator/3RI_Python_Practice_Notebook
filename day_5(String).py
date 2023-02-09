# name = "Ashutosh"
# name2 = "Python"
# l = "python class"
# print(type(name))
# print(len(name))
# print(name[0].lower())
# a = name2[0].lower()
# print(a)
# print(name[:4], "is my name")
# print(l[3])  # h
# print(l[7])  # c
# print(l[-3])  # a
# print(l[2:9])  # t---l
# print(l[:9])  # p---l
# print(l[3:])  # h---l
# print(l[-8:-3])  # o--l

# var = "My favorite program language is python programming language"
# print(var[32:38])
# favorite = var[32:38]
# print(favorite)
# print(var[-27:-21])
# l1 = 'python class '
# l2 = "This is"
# # Concatenation Operator (+)
# l3 = l1 + l2
# print(l1)
# print(l2)
# print(l3)
# l3 = l1*2  # repetition operator (*)
# print(l3)

l1 = "python class"
# print("py" in l1)
# print("ok" in l1)
# print("ok" not in l1)
# print("on" not in l1)

"""
ask = input("Enter a character to check whether, it is present or not\n")
if ask in l1:
    print("Yes", ask, "is present")
else:
    print(ask, "is not present")
"""
# print(l1.capitalize())
# print(l1.title())
# print(l1.upper())
# print(l1.lower())
# print(l1.isupper())
# print(l1.islower())

"""for i in l1:
    print(i)"""

"""
length = len(l1)
print(len(l1))
i = 0
while i < len(l1):
    print(l1[i])
    i += 1
"""

# wap to print the vowels from the entered string
"""
var = input("Enter any string\n")
var = var.lower()
for i in var:
    if i == 'a' or i == "e" or i == "i" or i == "o" or i == "u":
        print(i)

"""
"""
var = input("Enter any string\n")
var = var.lower()
for i in var:
    if i in "aeiou":
        print(i)
"""

# wap to print how many vowels are present in the entered string
"""
var = input("Enter any string\n")
var = var.lower()
var2 = 0
for i in var:
    if i == 'a' or i == "e" or i == "i" or i == "o" or i == "u":
        var2 += 1
print(var2)
"""

# wap to print how many small letters are present in your name
"""
var = input("Enter any string\n")
var2 = 0
for i in var:
    if i.islower():
        var2 += 1
print(var2)
"""
# Write a program to print your entered name in reverse order.

name = input("Enter your name\n")
"""
count = len(name) - 1
while count >= 0:
    print(name[count], end="")
    count = count - 1   
"""
# OR

"""
print(name[::-1])
"""
# Write a program to print every third character of entered string.
"""
print(name[::3])
"""
# Write a program to find the number of characters present in string without using len()
"""
char_count = 0
for i in name:
    char_count += 1
print(char_count, "no. of characters")
"""
# Write a program to print the number of vowels present in entered string.
"""
vowels = 0
name = name.lower()
for i in name:
    if i in "aeiou":
        vowels += 1
print(vowels, "no. of vowels")
"""
# Write a program to find a character present in string or not?if present in which index it is present.
# and how many times it is present.
"""
char = input("Enter the name of the character you want to find\n")
count1 = 0
for i in name:
    if i == char:
        count1 += 1
if count1 >= 0:
    print(char, "is present")
else:
    print(char, "not present")

print(name.count(char), "no. of times", char, "is present")
print(char, "is present at", name.index(char), "index")
print(count1, "no. of times character is present")
"""