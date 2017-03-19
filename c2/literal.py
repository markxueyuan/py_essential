##
v = "Jalape\u00f1o"
s = "Jalape\N{LATIN SMALL LETTER N WITH TILDE}o"
print(v)
print(s)

# http://www.unicode.org/charts

# raw strings

path = r'C:\newdata\tests'  # raw strings

a = r"\u1234"  # odd for unicode string
b = r"\\u1234"  # seven-character string

# byte literal

c = b"Jalape\xc3\xb1o"  # multiple byte sequence represents a single character
d = "Jalape\xc3\xb1o"  # a string of single bytes
e = "Jalapeño"
print(c.decode())
print(d)
print(e.encode())
print(c == d)



