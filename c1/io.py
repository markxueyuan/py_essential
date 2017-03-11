# What is 'method'?
# why is it necessary to close a file after open it?

# write

from __future__ import print_function

numyears = 20
rate = .05
principal = 1000
year = 0

f = open("c1/demo.txt", "w")  # the open function returns a new file object

f.write("%s" % "The compounds with rate .05")  # invoke method `write' on this object
print(file=f)  # print a new line
print("Year, Principal", file=f)  # write header

while year <= numyears:
    print("%3d, %0.2f" % (year, principal), file=f)
    principal *= 1 + rate
    year += 1

f.close()

# read

g = open("c1/demo.txt")
line = g.readline()

while line:
    print(line, end='')  # print line in python3
    line = g.readline()  # read the next line
g.close()

# for statement for reading lines

for line in open("c1/demo.txt"):
    print(line)




