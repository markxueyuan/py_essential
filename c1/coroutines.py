# This script is a demonstration of what asynchronous and concurrent
# programming is like.

# Used in scenario when one part of program is producing data to be
# consumed by another part of the program.

# coroutine takes a (imaginary) sequence as input.

import time
import _thread # 'import thread' in python 2


def print_matches(matchtext):
    print("Looking for", matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(matchtext, ": ", line)
        time.sleep(0.333)   # sleep for 0.333 seconds before next round


def tail(f):
    f.seek(0, 2)  # 2 means relative to the end of file,
    # 0 is the offset position of read/write pointer
    while True:
        line = f.readline()
        if not line:
            continue  # to start a new loop in 'while'
        yield line


def s():
    time.sleep(1.5)

def simulate_log(fileName):
    f = open(fileName, "a") # "a" for opening file in appending mode
    f.write("I am little python\n")
    s()
    f.write("I am little nothing\n")
    s()
    f.write("I am little guido\n")
    s()
    f.write("I am little jython\n")
    s()
    f.write("I am python, guido and jython\n")
    f.close()


# show basic mechanism of how coroutines work.


matcher = print_matches("python")  # set up a 'waiter' for callback functions

matcher.__next__()  # execute to the first (yield), wait for new message

matcher.send("Hello World")  # send info to (yield), execute to the next round (yield)
s()
matcher.send("python is cool")
s()
matcher.send("yow!")
s()
matcher.send("What do you think about python?")

matcher.close()  # close the 'waiter'


# simulate a log

a = "demo3.txt",

_thread.start_new_thread(simulate_log, a)

# match the update of the log

matchers = [
    print_matches("python"),
    print_matches("guido"),
    print_matches("jython")
]

for m in matchers:
    m.__next__()

log = tail(open("demo3.txt"))

for l in log:
    for m in matchers:
        m.send(l)


"""

writer ------> log <------ matcher

"""



