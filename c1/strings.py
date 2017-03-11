# what does '\n' mean?
# what does a[:-1] mean? (a is a string)
# What's the difference between str() and repr()?

##

a = "Hello 'World'\n"
b = '"This" is possible\n'
c = """not
on
the same line\n"""  # triple-quoted strings allow multiple line

print(a, b, c)

# indexing

d = a[6]  # strings are sequences of characters indexed by integers

print(d)

# substring
u = "0123456789"
u1 = u[:6] # not include the 6th
u2 = u[6:] # include the 6th
u3 = u[3:9]
print(u1)
print(u1, u2, u3)
print(u1, u2, u3, "\n")

# concatenate

g = a[:-1] + ' test\n'
print(g)

# string -> numeric

x = "37"
y = "42"
z = x + y
u = int(x) + int(y)
f = float(x) + int(y)
print(z, " vs ", u, "vs", f)

# numeric -> string

x = 3.4
a = str(x)   # str() returns values human-readable
b = repr(x)  # repr() generate representations read by the interpreter
c = format(x, "0.5f")
print(a, b, c)












