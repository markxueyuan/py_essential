# An object is a sort of dictionary

class TruthFinder:
    def __init__(self):
        self.content = 1

    @property
    def value(self):
        return self.content


t = TruthFinder()
print(t.value)
print(t.__dict__)

## dictionaries are objects having behaviors

m = t.__dict__

m.get('content')
m.get('coop', 'not found')
m.setdefault('foo', 'hoo')
m.setdefault('content', 'invalid')
print(t.__dict__)

## iterator

m.keys() # generates an iterator of keys
m.values() # iterator of values
m.items() # iterator of tuples of keys and values

for k in m:
    print(m[k])

for k in m.keys():
    print(m[k])

for v in m.values():
    print(v)

for k,v in m.items():
    print("{} has value {}".format(k, v))

# dictionary is mutable
m['content'] += 1

# dictionary can use almost  all as key except the list
class AnObject():
    def __init__(self, avalue):
        self.avalue = avalue

my_object = AnObject(12)
my_map = {('abc', 3):3, my_object:7, 3:4}
print(my_map[my_object])

try:
    my_map[[1,2,3]] = 11
except Exception as e:
    print(dir(e))