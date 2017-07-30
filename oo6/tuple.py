# Tuples are immutable
# The benefit of immutability is that we can use them as keys in dictionaries,
# and in other locations where an object requires an hash value.

# Behavior cannot be stored in a tuple


# create a tuple
stock = "FB", 75.00, 75.03, 74.90
# or
stock2 = ("FB", 75.00, 75.03, 74.90)

print(stock == stock2)

# parentheses are required for wrapping tuples in other objects

import datetime

def middle(stock, date):
    symbol, current, high, low = stock # learn tuple unpacking
    return ((high + low) / 2, date)

mid_value, date = middle(("FB", 75.00, 75.03, 74.90), datetime.date(2014, 10, 31))

# access tuple
high = stock2[2]

########### namedtuple

# namedtuple returns a class-like object, which can be instantiated as many times as possible

from collections import namedtuple

Stock = namedtuple("Stock", 'symbol current high low')

stock1 = Stock("FB", 75.00, 75.03, 74.90)
stock2 = Stock(symbol='FB', current=75.00, high=75.30, low=74.90)
stock3 = Stock('FB', current=75.00,  high=75.30, low=74.90)
#positional argument can only go ahead of keyword argument

print(stock1.high)
symbol, current, high, low = stock2

# Named tuples are perfect for many data only representations, but it is immutable, so it's difficult to modify

try:
    stock1.high = 77.00
except AttributeError as e:
    print(e)


# Hashable object usually have a defined algorithm that converts the object in to a unique integer
# for rapid lookup.

#########################    use defaultdict

# Using scenario

def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequencies.setdefault(letter, 0)
        frequencies[letter] += 1
    return frequencies

# which has to test if it has a value each time.
# Instead we can use defaultdict

from collections import defaultdict

def letter_frequency2(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

# The defaultdict accepts a function in its constructor.
# Whenever a key is accessed that is not already in the dictionary,
# it calls that function, with no parameters, to create a default value

# Here it calls int, which is a constructor of int object.

class TupleCounter():
    def __init__(self):
        self.counter = 0

    def tuple_count(self):
        self.counter += 1
        return (self.counter, [])

d = defaultdict(TupleCounter().tuple_count)

d['a'][1].append("hello")
d['b'][1].append('world')
d['a'][1].append('kitty')
print(d)


########################### counter


# count specific instances in an iterable

from collections import Counter

def letter_frequency3(sentence):
    return Counter(sentence)
































