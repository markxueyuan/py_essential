# Why do I set up list first then turn it into tuple?


# copy csv file in to list-tuple-combined data structure
# run 'python readCSV.py demo.txt' in console to see how the code works

import sys

if len(sys.argv) != 2:
    print("Please supply a file name")
    raise SystemExit(1)

f = open(sys.argv[1])

header = f.readline().split(',')  # read and split the header line
num = len(header)  # count the number of fields
col = []  # where tuples to be put
lines = f.readlines()  # read all lines in

for l in lines:
    row = l.split(',')  # split data by comma
    t = []  # empty list to put split data in
    i = 0
    while i < num:
        t.append(row[i].strip())  # put stripped split data in
        i += 1
    t = tuple(t)  # change list to tuple
    col.append(t)  # add to the collection


# should be deleted in practical use

print(repr(col))











