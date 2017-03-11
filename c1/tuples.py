# Why tuple should be viewed as a single object (immutable)
# rather than a collection?

# Why tuples are needed although we have lists?


first_name = "XX"
last_name = "YY"
phone = '12345678'

##
stock = ('GOOG', 100, 490.10)
address = ('www.python.org', 8080)
person = (first_name, last_name, phone)

print(stock)
print(address)
print(person)


stock = 'GOOG', 100, 490.10 # tuples are like Stata's local macro
address = 'www.python.org', 8080
person = first_name, last_name, phone

print(stock)
print(address)
print(person)

##

item = 'a'
a = ()  # 0 tuple
b = (item,)  # 1-tuple, comma cannot be omitted
c = item,  # 1-tuple, comma cannot be omitted
e = (item) # the parentheses is redundant

print(a)
print(b)
print(c)
print(e)
print(e == item)
print(c == item)

# unpack tuples

name, shares, price = stock
host, port = address
first_name, last_name, phone = person

print(shares)
print(port)
print(last_name)

# use lists and tuples together:
# refer to readCSV.py







