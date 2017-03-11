# What is local scope?


def remainder(a, b):
    q = a // b  # // returns the quotient
    r = a - q * b
    return r


def divide(a, b):
    q = a // b  # // returns the quotient
    r = a - q * b
    return (q, r)


print(remainder(10, 3))
print(divide(10, 3))

q, r = divide(10, 3)  # unpack
print(q)


# assign default value

def connect(host, port, timeout=300):
    print(host)
    print(port)
    print(timeout)

connect('www.python.org', 3030, 200)
connect('www.python.org', 3030)

connect(port=3030, host="www.python.org")  # arbitrary order

# alter global variable inside a function

count = 0


def foo():
    global count
    count += 1

for x in range(0, 10000):
    foo()

print(count)








