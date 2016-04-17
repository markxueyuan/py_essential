# documentation strings


def fact(n):
    """This function computes a factorial"""
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)  # recursive call

print(fact(5))

print(fact.__doc__)  # to see the documentation strings



