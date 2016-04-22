# callable types represent objects that support the function call operation
# () is the function call operator
# There are four callable types:
# 1. user-defined functions
# 2. methods
# 3. built-in functions and methods
# 4. some class and instance objects

gl = "for demonstration"

################ user-defined functions


def foo(x, y):
    """What the hell?"""
    return x + y

print(foo(3, 4))


print((lambda x, y: x * y)(3, 4))  # lambda defines unanimous function


def bar(x, y):
    """ returns a function instead of a value,
    forming a closure for the returned anonymous function"""
    return lambda z: (x + z) * y


# attributes of user defined function

print(foo.__doc__)
print(foo.__name__)
print(foo.__dict__)  # dictionary containing function attributes
print(foo.__code__)  # byte compiled codes
print(foo.__defaults__)  # tuple containing default arguments
print(foo.__globals__)  # global variables

print(bar(3, 4)(5))  # returns (3 + 5) * 4
print(bar(3, 4).__closure__)  # show the closure created by calling bar()

##################### methods

# __Methods__ are functions defined inside a class definition

# __Instance Methods__ operate on instance. 'self' is first argument

# __Class Methods__ operate on classes themselves as objects

# __Static Methods__ receive no instance or class object as first arg


class Foo(object):
    def __init__(self, arg):  # define an instance method, using self as first argument
        self.foo = [arg]

    def add(self, arg): # define an instance method, add an element
        """documentation string of method"""
        self.foo.append(arg)

    @classmethod
    def default(cls):  # define an class method, using cls as first argument
        return cls('default')  # Foo('default')

    @staticmethod
    def self_made(arg):  # define an static method
        return Foo(arg)  # recursively calls the instance method __init__

    def __str__(self):  # to define the string representation of the object
        return str(self.foo)


print(Foo(3))
print(Foo.default())
print(Foo.self_made(4))
f = Foo(3)
f.add('hehe')
print(f)

# both instance and class method belong to the types.MethodType

# how object attribute lookup (.) works

f = Foo(3)
# Invoking a method includes:
# 1. lookup on an object
o = f.add  # bound method
# 2. make a function call
o('haha')  # () is the function call operator
print(f)

# __bound method__ is a callable object that wraps both an function (method)
# and an associated instance

# loop up can also occur on the class itself

oo = Foo.add  # unbound method
oo(f, "yeah")  # give the method self and other arguments
print(f)

# bound and unbound methods are both represented as
# an object of type types.MethodType
# (In python 3, unbound methods are just raw functions
# not wrapped by the object of MethodType)

# attributes of method object:

print(o.__doc__, oo.__doc__)
print(o.__name__, oo.__name__)
print(o.__class__, oo.__class__)  # class, function

print(o.__func__) # oo.__func__ is not allowed because
# 'function' object has no attribute '__func__'

print(o.__self__)  # 'function' has no attribute '__self__'



############### built-in functions and methods

# represent functions and methods implemented in c and c++

print(len.__doc__)
print(len.__name__)
l = [2, 3]
print(l.append.__self__)
print(len.__self__)

############### callable class and instance

class Aaa(object):
    def __init__(self):
        self.aaa = []

    def add(self, arg):
        self.aaa.append(arg)

    def __call__(self, index):
        return self.aaa[index]

    def __str__(self):
        return str(self.aaa)


a = Aaa()
for i in range(1, 6): a.add(i)
print(a)
print(a(2))  # a is now a callable instance












