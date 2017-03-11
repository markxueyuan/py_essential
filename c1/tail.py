# What's the difference between 'continue' and 'break'?

# mimic Unix pipeline 'tail -f fileName | grep searchText'

import time


def tail(f):
    f.seek(0, 2)  # 2 means relative to the end of file,
    # 0 is the offset position of read/write pointer
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue  # to start a new loop in 'while'
        yield line


def grep(lines, searchtext):
    for l in lines:
        if searchtext in l:
            yield l

t = tail(open("demo3.txt"))

pylines = grep(t, "python")

for line in pylines:
    print(line, end="")

""" t = tail(open("c1/demo3.txt"))

pylines = grep(t, "python")

for line in pylines:
    print(line, end="")

Theoretically the above code should work.

However I cannot test them because python locks the file so that I cannot
edit the txt file.

"""

# grep is a useful command in Unix


"""
def grep2(filename, searchtext):
    print("Starts!")
    f = open(filename)
    for l in f:
        if searchtext in l:
            yield l
        time.sleep(1.5)

c = grep2("c1/demo3.txt", "python")

for i in range(3):
    print(c.__next__(), end="")
"""


