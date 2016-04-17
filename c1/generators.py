# Why generator are useful in pipelines, streams or data flow?
# (Hint: due to its laziness)

# Can you give the stack trace of the code?


def countdown(n):
    print("Counting Down!")
    while n > 0:
        yield n
        # print("Still ", n)  # adding this print provider insight on how generator works
        n -= 1  # means n = n - 1


c = countdown(1000)  # imagine it returns an unseen object like [1000, 999, 998, ....]


# call method next on c returns the element successively:

for i in range(10):
    print(c.__next__())  # print c.next() in python 2

"""
1. c = countdown(1000) generates a local scope designate 1000 to n
    n <--- 1000
but the body of the function is not called.

2. when c.next() is executed for the first time,
the code of the body is executed to the `yield' line
    because n <--- 1000 in the local scope, so 1000 is returned.
the code returns and suspends at the `yield' line



3. when c.next() is executed for the second time,
the execution resumes to the next line: print("Still ", 1000)
execute n -= 1, n <--- 999 in the local scope
because n > 0, predicate n > 0 is met
while loop starts a second round
the execution suspends at the line of `yield n'

4. when c.next() is executed for the third time, ...

5. ...

...


"""

# in operator + generator

for i in countdown(5):
    print(i, end="")

# Unix tail
# refer to tail.py
