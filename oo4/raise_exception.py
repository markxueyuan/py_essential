# All exception classes inherit from a built-in BaseException class


# All (?) built-in exceptions end with the name Error

# All (?) error classes have Exception as their superclass

# Exception extends BaseException

class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2: # % is the modulus operator
            raise ValueError("Only even numbers can be added")
        super().append(integer)

def main():
    eo = EvenOnly()
    try:
        eo.append("a string")
    except TypeError as e:
        print(e)
    try:
        eo.append(3)
    except ValueError as e:
        print(e)
    eo.append(8)
    print(eo)


def no_return():
    print("a")
    raise Exception("wrong")
    print("not printed")
    return "not returned"

def call_exceptor():
    print("b")
    no_return()
    print("not reachable")


# should be able to interpret exception Traceback
# exactly