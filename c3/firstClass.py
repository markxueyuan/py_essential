# What does _first class_ mean?
# 1. All objects named by an identifier have equal status
# 2. All objects that can be named can be treated as data

import math


items = {
    'number': 42,
    'text': "Hello World"
}

items['function'] = abs  # add the abs() function
items['mod'] = math  # add the module
items['error'] = ValueError  # add an exception type
nums = [1, 2, 3, 4]
items['append'] = nums.append  # add a method of another object

print(items)

print(items["function"](-45))  # executes abs(-45)
print(items['mod'].sqrt(9))  # executes math.sqrt(9)

try:                  # refer to exceptions.py for try-catch syntax
    x = int('a lot')
except items["error"] as e:  # except ValueError as e:
    print("Couldn't convert")

items['append'](100)  # nums.append(100)
print(nums)

# appreciate the beauty that everything in python is first-class

line = "GOOG,100,350.9"
field_types = [str, int, float]
raw_fields = line.split(',')
# zip combines two (several) sequences in to sequece of tuples
fields = [ty(val) for ty, val in zip(field_types, raw_fields)] # list comprehension
print([type(fld) is ty for fld, ty in zip(fields, field_types)])
print([type(fld) for fld in fields])





