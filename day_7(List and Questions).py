"""l1 = []
l2 = [7, 8, 9, 9]
l3 = ["abc", "par"]
l4 = ["aca", 445]
print(type(l1))
print(type(l2))
print(type(l3))
print(type(l4))
print(l2)"""

# l = [12, 67, 45, 89, 23, 45, 890, 900, 45]
# n = [8, 9, 0]
# print(l)
# l[2] = 56
# l[2:6] = [3, 7, 9, 0]
# l.clear()
# l.pop(4)
# del l[3]
# l.remove(45)
# l.append(74)
# l.insert(3, 457)
# l.extend(n)
# l.reverse()
# l.sort()
# print(l)

# Wap to concatenate two lists
"""
l1 = [23, 45, 67, 89, 100]
l2 = [6, 7, 8, 9, 1, 0]
l3 = l1 + l2
print(l3)
"""

# Wap to repeat a list 3 times
"""
l4 = [4, 3, 56, 73, 9]
l5 = 3*l4
print(l5)
"""

# Wap to check the entered element is present in list or not
"""
num = int(input("Enter an element to check whether it is present in list or not"))
list1 = [45, 6, 72, 43, 7]
if num in list1:
    print(num, "present in list")
else:
    print("not present")
"""


"""for i in l:
    if i % 2 == 0:
        print(i)
"""
"""
i = 0
while i >= 0:
    if l[i] % 2 == 0:
        print(l[i])
    i = i + 1
    if i >= len(l):
        break
"""
# OR

"""
count = 0
while count < len(l):
    if l[count] % 2 == 0:
        print(l[count])
    count += 1
"""

"""
print(l[2])  # --> 45
print(l[8])  # --> 45
print(l[-3])  # --> 890
print(l[2:7])  # --> [45, 89, 23, 45, 890]
print(l[-6:])  # --> [89, 23, 45, 890, 900, 45]
"""
# Tuple

t1 = (56, 45, 56, 89)
print(type(t1))
l = [6, 7, 89]
t = tuple(l)
print(type(t))
print(t)
t = (8, 8, 0, 6)
l1 = list(t)
print(type(l1))
print(l1)
# t[2] = 900  # It will throw an error because tuple cannot be updated, delete, replaced
# del t[3]  # it will throw an error
