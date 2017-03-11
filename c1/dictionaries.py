# Two ways to look at a dictionary:
# 1. as a way to define object;
# 2. as a container for performing fast lookups.

# dictionary is an associative array (hash table/ map) that contains
# objects indexed by keys

stock = {
    "name": "GOOG",
    "shares": 100,
    "price": 490.10
}


##

name = stock["name"]
print(name)

value = stock["shares"] * stock["price"]
print(value)

stock["shares"] = 75
stock["date"] = "June 7, 2007"
print(repr(stock))

##

prices = {}
prices = dict()

prices = {
    "GOOG": 490.10,   # the key should be of \
    # hashable type: string in this case
    "AAAPL": 123.50,
    "IBM": 91.50,
    "MSFT": 52.13,
    "SCOX": 66.99
}

# in operator

if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0

print(p)

# which equals

p = prices.get("SCOX", 0.0)
print(p)

# get keys

syms = list(prices)
print(syms)

# delete

del prices["MSFT"]
print(prices)








