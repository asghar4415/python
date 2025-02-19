print("helloworld")

# Python is an interpreted language, so you can run the code directly from the command line.

# why python is so popular?
# 1. Easy to learn
# 2. Open source
# 3. High level language
# 4. Interpreted language
# 5. Object oriented language
# 6. Extensible


# basics of python

# we already know about the variables, functions, loops, conditions, etc.

x = input("Enter a number: ")
print(x)
y = input("Enter a number: ")
print(y)
print(f"sum of {x} and {y} is {int(x) + int(y)}")

# run with py basics.py


# loops:
# for loop
for i in range(5):
    print(f"{i}")

# we can also do range(1, 5) to start from 1 and end at 5
# we can also do range(1, 10, 2) to start from 1 and end at 10 and increment by 2


# OOPs concepts in python

# 1. Class
# a Class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).

# example:
# class ClassName:
#   var1 = 10
#   var2 = 20
#   def __init__(self):
#       print("constructor")
#   def method1(self):
#       self.var1 = 100
#       print("method1")
#   def method2(self):
#       self.var2 = 200
#       print("method2")

# self in above example is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# 2. Object
# An object is a collection of data (variables) and methods (functions) that act on the data. And, a class is a blueprint for the object.

# example:
# obj = ClassName()
# obj.method1()
# obj.method2()
