################################# len()

# function len() is better than method __len__() for:
# 1. __len()__ looks up the __getattribute__ first
# 2. __getattribute__ may do something nastry like refusing access to __len__()
# 3. len() goes directly to __len__()


############################## reversed()

# What is the minimum needed for an object to be iterable?

class CustomSequence():
    def __len__(self):
        return 5
    def __getitem__(self, item):
        return "x{}".format(item)


a = CustomSequence()

for x in reversed(a):
    print(x)


### [Seems that without this reversed(), for loop will never end,
###  and __len__ never be called.]
### the reason is that the __iter__ is not implemented
normal_list = [1, 2, 3, 4, 5]

class FunkyBackwards():
    def __reversed__(self):
        return "BACKWARDS!"


for seq in CustomSequence(), normal_list, FunkyBackwards():
    print("\n{}: ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")
print('\n')


# the reverse() function first searches for the __reversed__(),
# if it doesn't exist, go to __len__ and __getitem__


###################### enumerate()

# for loop doesn't provide index, enumerate does.
# enumerate creates a sequence of tuple, where the first in
# the tuple is the index and the second is the original item

a = ['a', 'b', 'c']

for n, x in enumerate(a):
    print(n, x)

#################### all(), any()
all(reversed(CustomSequence()))
all((True, False))
any((True, False))

######################

# eval, exec, compile execute string as code inside the interpreter


# hasattr, getattr, delattr is to manipulate attribute by their string names

##################### zip

z = zip([1, 2, 3], [4, 5, 6, 7, 8])

for x in z:
    print(x)


