from sys import getrefcount

# reference count
a = 37
b = a  # increase reference count on 37
c = []
c.append(b)  # increase reference count on 37

print(getrefcount(a)) # the reference count is much higher than you might imagine

del a  # decrease reference count of 37
b = 42  # decrease reference count of 37
c[0] = 2.0  # decrease reference count of 37

##
try: print(getrefcount(a))  # a has been deleted, so we need to try-and-catch
except NameError as e:
    print(e)

# circular dependency

a = {}
b = {}
a['b'] = b
b['a'] = a
print(a, b)  # a and b are lazily printed
del a
del b

# Although names used to refer the objects have been destroyed,
# and the reference count has decreased,
# the references to each other still exist
# resulting in a #memory leak#

# The interpreter periodically searches for cycles of inaccessible object
# and deletes them. This is called #garbage collection#, #gc.










