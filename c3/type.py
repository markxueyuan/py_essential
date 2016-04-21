# terminology

# the #identity of an object is a pointer to its location in memory

# The #type or #class of an object describes the internal representation
# of the object as well as the methods and operations that it supports.

# The object of a particular type is called an #instance of that type.

# The object is #mutable if its value can be modified.
# The object is #immutable if its value cannot be modified.

# An object that contains references to other objects is said to be
# a #container or #collection

# An #attribute is a value associated with an object.
# A #method is a function that performs some sort of operation on an
# object when the method is invoked as a function

from copy import deepcopy

a = 3 + 4j  # a complex number
r = a.real  # get the attribute
print(r)

b = [1, 2, 3]
b.append(7)  # use the method
print(b)

##

print(id(a), id(b))  # id shows object's location in memory

c = a
print(c is a)  # is operator compares the identity of two objects
print(b is a)

print(type(a))  # returns the type of an object
print(type(b))


def compare(a, b):
    if a is b:
        return "The two are the same object."
    elif a == b:
        return "The two have the same value but are not the same object."
    elif type(a) is type(b):
        return "The two have the same type but don't have the same value."
    else:
        return "The two are quite different."

d = 3 + 4j
print(compare(a, b))
print(compare(a, c))
print(compare(c, d))


# The type of an object is itself an object known as the object's class

print(type(a) is type(b))  # to see if a and b's class is the same object
print(id(type(a)))  # type (class) also has its position in memory

# All type objects are assigned names that can be used to perform type checking

print(id(list)) # list is the name of type object

if type(b) is list:
    b.append(777)
print(b)

e = {"a": 2, "b": 3}
if type(e) is dict:
    e.update({"a": 3, "b": 4})
    e.update({"b": 5, "c": 6})
print(e)

##

if isinstance(b, list):  # isinstance is aware of inheritance
    b.append("6")
print(b)
if isinstance(e, dict):
    e.update({"e": 9})
print(e)

# references and copies

u = 2  # create immutable objects
v = u  # assignment u to v creates a #copy of u
print(u is v)
print(id(u) == id(v))
u = 3
print(v)  # although u is changed to 3, v is still 2

x = [1, 2, 3, 4]  # create mutable objects
y = x  # y is a reference to x
print(y is x)
y[2] = -100
print(x)  # x changes as well
print(x is y)

"""
immutable -------- copy
mutable   -------- reference
"""

# #shalow copy# creates a new object but populate it with references to the items contained in the original object

a = [1, 2, [3, 4]]

b = list(a)  # shallow copy
print(b is a)
print(b)

a[1] = 3  # a changes its reference in its second slot
print(b)  # b still keeps the old reference in its second slot

a[2][1] = 5
print(a)  # a changes the content of its third slot
print(b)  # b changes as well for it keeps the reference in shallow copy

b.append(100)
print("b is:", b)
print("a is:", a)

b[2][0] = -100
print("a is:", a)
print("b is:", b)

# A #deep copy# creates a new object and recursively copies all
# the objects it contains

c = deepcopy(a)
c[2][1] = -50
print(c)
print(a)  # a is still unchanged













