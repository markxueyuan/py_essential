# What is 'method'?
# why is it necessary to close a file after open it?


# write

numyears = 20
rate = .05
principal = 1000
year = 0

f = open("demo.txt", "w")  # the open function returns a new file object

# f.write("%s" % "The compounds with rate .05")  # invoke method `write' on this object
# print(file=f)  # print a new line
print("Year, Principal", file=f)  # write header

while year <= numyears:
    print("%3d, %0.2f" % (year, principal), file=f)
    principal *= 1 + rate
    year += 1

f.close()

# read

g = open("demo.txt")
line = g.readline()

while line:
    print(line, end='')  # print line in python3
    line = g.readline()  # read the next line
g.close()


