# to run this file, run 'python ls1.2.py demo2.txt' in the console

import random
import sys

# write

f = open("demo2.txt", "w")

i = 0
while i < 50:
    f.write("%3d \n" % random.randint(0, 100))
    i += 1
f.close()

# read and calculate

if len(sys.argv) != 2:  # sys.argv returns a list ["ls1.2.py", "demo2.txt"]
    print("Please supply a filename")
    raise SystemExit(1)# to run this file, run 'python ls1.2.py demo2.txt' in the console



f = open(sys.argv[1])
lines = f.readlines()  # read all input lines into a list of strings
f.close()

fvalues = [float(l) for l in lines]  # list comprehension

"""
The codes  in the above line is the same as the follow:

fvalues = list()
for l in lines
    fvalues.append(float(l))

fvalues = [float(l) for l in f]

also works, because lines in f can be read using for loop

"""


print("The minimum value is ", min(fvalues))
print("The maximum value is ", max(fvalues))


