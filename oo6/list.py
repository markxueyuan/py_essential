# lists are used to store objects in order, this is the order in which they are inserted

import string

CHARACTERS = list(string.ascii_letters) + [" "]

def letter_frequency4(sentence):
    frequencies = [(c, 0) for c in CHARACTERS] # list comprehension
    unrecognized = 0

    for letter in sentence:
        try:
            index = CHARACTERS.index(letter)
            frequencies[index] = (letter, frequencies[index][1] + 1)
        except:
            unrecognized += 1

    return frequencies + [('unk', unrecognized)]

letter_frequency4("To be or not to be, that is a question.")


############ sorting lists

# Z comes before a

a = ['b', 'a', 'Y']
a.sort()

b =[('b','a'), ('a', 'b')] #first element of tuple matters
b.sort()
# you cannot sor the unorderable
c = ['a', 2]
try:
    c.sort()
except TypeError as e:
    print(e)


########### how to make object sortable?

class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < other.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)
    # which is for a prettier print


a = WeirdSortee('a', 4, True)
b = WeirdSortee('b', 3, True)
c = WeirdSortee('c', 2, True)
d = WeirdSortee('d', 1, True)

l= [a, b, c, d]
l
l.sort()
l

for i in l:
    i.sort_num = False

l.sort()
l



################### @total_ordering

from functools import total_ordering

@total_ordering
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < other.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)

    def __eq__(self, other):
        return all((
            self.string == other.string,
            self.number == other.number,
            self.sort_num == other.sort_num
        ))

# onlly __lt__ __eq__ needed to get other __ne__,
# __gt__, __le__, __ge__


############### customize sort orders

l= ['hello', 'Help', 'Helo']
l.sort(key=str.lower)
l

# str.lower(item) is equivalent to item.lower()
# try

class A:
    def __init__(self):
        pass
    def test(self):
        print('It works!')

a = A()
A.test(a)


from operator import itemgetter
# I guess this is the real body of [] operator

b =[('b','a'), ('a', 'b')]
b.sort(key=itemgetter(1))
b

# similarly there are attrgetter and methodcaller

