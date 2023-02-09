"""s = {23, 56, 78, 90, 23, 12}
s2 = {}  # it will be recognised as an dictionary
s3 = set()  # it will now become an empty set
print(type(s))
print(type(s2))
print(type(s3))"""

# Operations on set
"""
s1 = {12, 67, 89, 34, 77, 90}
s2 = {456, 890, 77, 12}
"""

# union operation
"""
s3 = s1 | s2
print(s3)
"""

# union function
"""
s3 = s1.union(s2)
print(s3)
"""

# intersection operation
"""
s3 = s1 & s2
print(s3)
"""

# intersection function
"""
s3 = s1.intersection(s2)
print(s3)
"""

# difference operation
"""
s3 = s1 - s2  # it will return the only value present in s1
print(s3)
"""

# difference function
"""
s3 = s1.difference(s2)
print(s3)
"""

# symmetric difference operation
"""
s3 = s1 ^ s2  # returns the value only present in s1 and s2 means common is removed
print(s3)
"""

# symmetric difference function
"""
s3 = s1.symmetric_difference(s2)
print(s3)
"""

# s1 = {12, 67, 89, 34, 77, 90}
# print(s1)
# s1.add(23)
# s1.update([67, 900, 34, 12])
# s1.clear()
# s1.discard(12)
# s1.discard(23)
# s1.remove(890)  # it will throw an exception if element not present
# print(s1)

# create a set having working day names.Check the Tuesday is working
"""
working_day_names = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
if "Tuesday" in working_day_names:
    print("Tuesday is present")
"""

# Dictionary
emp = {"id": 100, "name": "Bharthi"}
# print(emp)
# print(type(emp))
# emp["name"] = "abc"
# emp["contact"] = 532332132
emp.update({"name": "dsgdg", "contact": 132321321, "age": 30})
print(emp)
# emp.clear()
# del emp
# emp.popitem()
# emp.pop("id")
# del emp["id"]
# n = emp["id"]
# n = emp.get("id")
# print(n)
# print(emp)
"""
print(len(emp))
print(emp.keys())  # it will return list of keys
print(emp.items())  # it will return key, value pairs
print(emp.values())"""  # it will return list of values

# Write a Python script to check whether a given key already exists in a dictionary
"""
num = input("Enter a given key\n")
if num in emp:
    print(num, "is present")
else:
    print(num, "not present")
"""

# Write a Python program to sum all the items in a dictionary.
"""
dict1 = {'a': 100, 'b': 200, 'c': 300}
sum1 = 0
for i in dict1.values():
    sum1 = sum1 + i
print(sum1)
"""

# create a dictionary named students having name and rollno
# 1)print dictionary
# 2)add new element to dictionary - age
# 3)update the age of student to 14
# 4)delete the rollno
"""
l1 = list(dict1.values())
print(l1)
print(sum(l1))
student = {"name": "Ashutosh", "rollno": 6}
print(student)
student["age"] = 21
print(student)
student.update({"age": 14})
print(student)
del student["rollno"]
print(student)
"""
