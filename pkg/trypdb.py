import pdb
from sympy.abc import x, y

e = x + y + x

def A():
    b = 0
    pdb.set_trace()
    print(e)
    print(c)



def recursive_function(n=5, output='to be printed'):
    if n > 0:
        recursive_function(n-1)
    else:
        pdb.set_trace()
        print(output)
    return


# try commands: list, args, up

def calc(i, n):
    j = i * n
    return j

def f(n):
    for i in range(n):
        j = calc(i, n)
        print(i, j)
    return

def tt():
    pdb.set_trace()
    f(5)