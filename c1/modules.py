##

import c1.div

a, b = c1.div.divide(2305, 29)
print(a)

##

from c1.div import divide  # import one specific function

print(divide(2305, 29))

##

import c1.div as foo  # designate an alias

a, b = foo.divide(2305, 29)
print(b)

##

from c1.div import *
te()

# import class

import string
print(dir(string))

