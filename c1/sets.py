
##

s = set([3, 5, 9, 10])
print(s)

t = set("Hello")  # elements in set are unique
print(t)

u = set(('a', 'b', 'c'))
print(u)


##

a = t | s
b = t & s
c = t - s
d = t ^ s
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

