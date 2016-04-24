import dis
from random import randint
import math
import random

################### none type


def make_none():
    print("This function returns none.")

print(type(make_none()))

################### all numeric types are immutable

# bool
print(True == 1)  # true
print(True is 1)  # false
print(type(True), type(1))  # type name
print(id(True), id(False))  # position

# int
# in python 3, long are integrated into int

# float in python is double-precision (64 bit) IEEE 754
a = 3.1415926
print(a.as_integer_ratio())  # turns float into ratio of integers
print(a.hex())  # return the hexadecimal representation of an integer
print(float.fromhex('0x1.ffffp10'))  # fromhex is a static method

# complex number

x = 3 + 4j
print(x.real, x.imag, x.conjugate())

######################## sequences type
# __sequences__ represent ordered sets of objects indexed by non-negative integers
# including strings, lists, tuples

# strings and tuples are immutable
# lists allow intersection, deletion and substitution of elements
# all sequences support iteration

# operation common to all sequences
s= "0jalfjalfaz"

print(s[2:6], s[0:9:2], max(s), len(s))  # s[i:j:stride]
n = [2, 7, 2, 3, 6, 4, 9, 0]
print(sum(n))  # sum is valid to sequences of numeric
print(all(s))

c = [randint(0, 1) for i in range(10)]
print(any(c))

# operations applicable to mutable sequences
del n[0:7:2]
print(n)

# list methods
t = (2, 7, 9, 4, 6)
l = list(t)
l.append(9)
l.extend([12, 13])
print(l.count(9))
print(l.index(12))
l.insert(1, 8)
print(l.pop())
print(l.pop(2))
l.remove(4)
l.reverse()
l.sort()
print(l)
l.sort(reverse=True)
print(l)

##################################### strings
# page 41 - 44
# __byte strings__
# __unicode strings__ 16 bit
# __surrogate pair__

# place holder
a = "Your name is {0} and your age is {age}."
print(a.format("Mike", age=30))
print(a)

# string is immutable
s = "bilibili.com"
print(s.capitalize()) #capitalize first character
print(s.center(20))
print(s.center(20, "@"))
print(s.ljust(30, "#"))
print(s.rjust(30, "#"))
print(s.count("bi"))
print(s.encode(encoding='utf-16'))
print(s.encode(encoding='utf-8'))
print(s.encode(encoding='utf-32'))

ss = 'communism'
print(ss.endswith('ism'))
print(ss.startswith("com"))

sss = 'ab   c'  # it is tab between b and c
print(sss.expandtabs())  # replaces tabs with spaces
print(s.find("il"))  # find the position where substring first appears
print(s.rfind("il"))  # find the position where substring last appears

uu = "IsThatReal2016"
print(uu.isalnum(), (uu + "?").isalnum(), uu.isalpha())

digit = "1234567890"
print(digit.isdigit())

xx = "jfalf232"
print(xx.islower(), uu.islower())
print(uu.swapcase())
print("\n\t ".isspace())
print("To Be Or Not To Be".istitle())
print("To Be or Not To Be".istitle())
print("AJODJOSJDOA".isupper())
print(",".join(list("abcde")))
print(",".join("abcde"))
print("a,b,c,d,e".split(","))
print("a,b,c,d,e".split(",", 2))
print("a,b,c,d,e".rsplit(",", 2))
print("a,b\nc,d,e".splitlines(2))

ux = " ajfalf\n"
print(ux.strip() == ux.lstrip())  # lstrip only removes the leading spaces

email = "ziyaajiang@gmail.com"
print(email.partition("@"))  # returns a tuple (head, sep, tail)
print(email.rpartition("@"))  # searches from the end of the string
print(s.replace("li", "oa"))
print(s.rindex("li"))  # find the index of last occurrence

z = '9876'
print(z.zfill(8))

########################## mapping

# you can use any immutable object as dictionary key

a = {
    1: 1,
    '2': 2,
    (3, 4): (3, 4)
}

print(a)

print(len(a))
print(a[(3, 4)])
a['5'] = ['hehe']
print(a)
del a['5']
print(a)
print(1 in a)
b = a.copy()  # seems a shallow copy
a.clear()
print(b)
print(a)
print(dict.fromkeys(['a', 'b', 'c'], 3))
print(a.fromkeys(['c', 'd'], 4))  # although static method
print(b.get((3, 4), "when not found"))
print(b.get((4, 5), "when not found"))
print(b.items()) # returns an iterator
print(b.keys())
print(b.pop('2'))
print(b.popitem())  # removes a random (k, v) and returns it as a tuple
print(b.setdefault((5, 6), 777))
m = {
    "hehe": 1,
    'lala': 2,
    3: 3
}
print(b.update(m))
print(b.values())

################# sets

# the item placed into sets must be immutable

s = set([1, 2, 3])  # mutable set
print(s)
x = frozenset(['a', 37, 'hello'])
print(x)
print(len(s))
t = s.copy()
u = set([2, 3, 4])
print(s.difference(u))  # returns all item in s, but not in u
print(s.intersection(u))
print(s.isdisjoint(u))
print(s.issubset(u))
print(s.issuperset(u))
print(s.symmetric_difference(u))
print(s.union(t))
s.add(8)
print(s)
s.difference_update(u)
print(s)
s.discard(8)
try:
    s.remove(9)
except KeyError as e:
    print(e)
print(s)
for i in range(8): s.add(i)
print(s)
s.pop()
print(s)
y = set()
for i in range(4, 16): y.add(i)
print(y)
s.symmetric_difference_update(y) # update s to the symmetric difference between s and y
print(s)
w = [i for i in range(16, 22)]
s.update(w)  # add items w to s
print(s)


##################### type of class


class Foo(object):
    """ The documentation of a class"""
    def __init__(self, arg):
        self.foo = arg
    c = 3.1415926


print(type(Foo))  # class is itself an object whose type is type

# type object's attribute

print(Foo.__doc__)
print(Foo.__name__)
print(Foo.__bases__)  # tuple of base classes
print(Foo.__dict__)  # class method and variables
print(Foo.__module__)

# type of instance
f = Foo('h')
print(type(f))  # the type of an instance is the class that defined it

# attribute of instance
print(f.__class__)
print(f.__dict__)

################ modules

# The __module type__ is a container that holds objects loaded with the import statement
# Modules defines a namespace that's implemented using a dictionary
# accessible in the attribute __dict__

print(math.__dict__)

# whenever an attribute of a module is referenced,
# it's translated into a dictionary lookup:
a = math.ceil
b = math.__dict__['ceil']
print(a is b)

print(math.__doc__)
print(math.__name__)
print(random.__file__)  # the file from which the module was loaded
# print(m.__path__) # only defined when the module refer to a package


############### bytecode

# __bytecode__ represents raw byte-compiled executable code

# refer to: https://www.reddit.com/r/Python/comments/1rfrfd/what_is_bytecode/
# video lecture: https://www.youtube.com/watch?v=0IzXcjHs-P8

def gunk(a=1, *args, b=3):
    print(args)
    c = None   # local vars
    d = 1      # cell vars

    def hehe():
        nonlocal d
        print(d)
    return (a + b, c)

print(dis.dis(gunk))  # dissemble gunk to bytecode
c = gunk.__code__
print(c)
print(type(c))  # class 'code'
print(dir(c))  # all the attributes of code object
print(c.co_name)  # name
print(c.co_code)  # string representing raw byte code
print([x for x in c.co_code])  # integer representation of the byte code
print(c.co_argcount)  # number of positional argument
print(c.co_nlocals)  # number of local variables of the function
print(c.co_varnames)  # names of local variables
print(c.co_cellvars)  # variables referenced by nested functions
print(c.co_freevars)  # free variables used by nested functions
print(c.co_consts)  # the literals used by the bytecode
print(c.co_names)  # names used by the bytecode
print(c.co_filename)  # name of the file in which the code was compiled
print(c.co_firstlineno)  # first line number of the function
print(c.co_lnotab)  # String encoding bytecode offsets to line numbers
print(c.co_stacksize)  # required stack size
print(c.co_flags)  # flags to interpreters.

################# frame object


################# traceback object

################# generator objects

def myrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in myrange(5):
    print(i, end="")

print()

m = myrange(5)
print(m.__next__())

################ slice object

a = [i for i in range(10)]
print(a[2:8:2])  # slices in extended slice syntax
s = slice(2, 8, 2)  # build a slice object
print(type(s))

print(s.start)
print(s.stop)
print(s.step)
print(s.indices(100))  # how slice would be applied to the sequence of that length
print(s.indices(6))

############### ellipsis object


class Example(object):
    def __getitem__(self, index):
        return index
e = Example()
b = e[3, ..., 4]
x, y, z = b
print(type(y))














































