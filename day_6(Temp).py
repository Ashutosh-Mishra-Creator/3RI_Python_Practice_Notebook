# data = '121414'
# data = '121t414'
"""
if data.isdigit():
    print("yes correct")
else:
    print("not correct")
"""
# data = ' '
# if data.isspace():
#     print("yes space")
# else:
#     print("not")

# data = "sadad"
# if data.isalpha():
#     print("alpha")
# else:
#     print("no")

# wap taking society name from user and count
# no. of alphabets
# no. of digits
# no. of spaces
# no. of special character
"""
num1 = input("Enter your Society name\n")
alphabets = 0
digit = 0
spaces = 0
spe_char = 0
for i in num1:
    if i.isdigit():
        digit += 1
    elif i.isspace():
        spaces += 1
    elif i.isalpha():
        alphabets += 1
    else:
        spe_char += 1
print(alphabets, "no. of alphabets")
print(digit, "no. of digits")
print(spaces, "no. of spaces")
print(spe_char, "no. of special character")
"""

l = "python, language, python, python, python"
# print(l.count("python"))
# print(l.find("python"))
# print(l.index('python123'))
print(l.replace('python', 'java', 2))
print(l.split(','))
