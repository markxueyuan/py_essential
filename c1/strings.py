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

a1 = a[:5]
a2 = a[6:]
a3 = a[3:9]
print(a1, a2, a3, "\n")

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












