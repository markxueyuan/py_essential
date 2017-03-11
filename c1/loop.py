# Why we say xrange() (in py2) or range() (in py3) is lazy?

for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("2 to the %d power is %d" % (n, 2**n))

for n in range(1, 10):  # shortcut
    print("2 to the %d power is %d" % (n, 2**n))

a = range(5)
b = range(1, 8)
c = range(0, 14, 3)
d = range(8, 1, -1)


v = [a, b, c, d]
for i in v:
    print(list(i))

# for loop

a = "Hello World"

for c in a:
    print(c)

b = ["Dave", "Mark", "Ann", "Phil"]

for name in b:
    print(name)

prices = {
    "GOOG": 490.10,
    "AAAPL": 123.50,
    "IBM": 91.50,
    "MSFT": 52.13
}

for p in prices:
    print(p, prices[p])

f = open("c1/demo.txt")

for l in f:
    print(l, end="")  # delete the \n at the end of the line

# compare to:

f = open("c1/demo.txt")

for l in f:
    print(l)  # delete the \n at the end of the line




