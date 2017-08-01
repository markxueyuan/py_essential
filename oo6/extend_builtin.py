# Why using syntactic sugar to makes it
# look less objected-oriented

# 1
a = 2
b = 3
c = a + b
c = a.__add__(b)

# 2
l = [0]
l[0] = 5
l.__setitem__(0,6)

# 3
d = {'a':3}
d['a']=4
d.__setitem__('a', 6)

# 4
alist = [2, 3, 4, 5]

for x in alist:
    print(x)

it = alist.__iter__()

while it.__length_hint__() > 0:
    x = it.__next__()
    print(x)

# the double-underscores remind us there is a better
# syntax out there

class SillyInt(int):
    def __add__(self, other):
        return 0

a = SillyInt('1')
b = SillyInt('2')
a + b

# We can add __add__ method to any class we write,
# then if we use the + operator, __add__ method is called

# to use x in y syntax, implement __contains__ method

# to use a[i] = b syntax, apply __setitem__ method
# to sue a = b[j] syntax, apply __getitem__ method

help(list.__add__)

# refer to oo3.abstract_base_class

# It is not guaranteed that any subclass will call that initializer
# therefore we use __new__


from collections import KeysView, ItemsView, ValuesView

class DictSorted(dict):
    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, val):
        """self[key] = val syntax"""
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        super().__setitem__(key, val)

    def setdefault(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    def keys(self):
        return KeysView(self)

    def values(self):
        return ValuesView(self)

    def items(self):
        return ItemsView(self)

    def __iter__(self):
        """for x in self syntax"""
        return self.ordered_keys.__iter__()

    ## the View objects use the __iter__ method loop over the keys
    ## then use __getitem__ to retrieve the values

def main():
    ds = DictSorted()
    d = {}

    ds['a'] = 1
    ds['b'] = 2
    ds.setdefault('a', None)
    ds.setdefault('c', 3)

    d['a'] = 1
    d['b'] = 2
    d.setdefault('c', 3)

    for k in ds:
        print(ds[k])
    for k in d:
        print(d[k])

    for k, v in ds.items():
        print(k, v)

    for k, v in d.items():
        print(k, v)


### seems that in python 3.5, ordered keys have already been realized in normal dict

# However, there is still OrderDict to use:


from collections import OrderedDict

help(OrderedDict)































