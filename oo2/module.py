# absolute import

import oo2.product

product = oo2.product.Product()

from oo2.product import Product

product = Product()


from oo2 import product

product = product.Product()

# relative import

from .product import Product

p = Product()


# import via __init__
# refer to __init__file in this directory
from oo2 import db

db


## always put startup code in a function

# see the trick in initialize_database

from oo2.database import db1, initialize_database

initialize_database()
db1


## wrap startup code in main(),

class Process:
    """Need a while for startup"""
    pass

def main():
    p = Process()
    print("start process")

if __name__ == "__main__":
    main()

# the above code will not be implemented when imported by other name space


## class in function (inner class)

def format_string(string, formatter=None):
    '''Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string.'''
    class DefaultFormatter:
        """Format a string in title case"""
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)

def main():
    hello_string = "hello world, how are you today?"
    print(" input: ", hello_string)
    print("Output: ", format_string(hello_string))

if __name__ == "__main__":
    main()



