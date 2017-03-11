
##

s = set([3, 5, 9, 10])
print(s)

t = set("Hello")  # elements in set are unique
print("t is: ", t)

u = set(('a', 'b', 'c', 'l'))
print("u is: ", u)


##

a = t | u
b = t & u
c = t - u
d = t ^ u # symmetric difference \
# (items in t or s, but not both)
print(a)
print(b)
print(c)
print(d)

##

t.add('x')  # add single
print(t)

s.update([10, 37, 42])  # add multiple
print(s)

t.remove('H')
print(t)

