########## Bad object-oriented theory

# Myth: (java is the most notorious) Never access attributes directly.

class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    c = Color("#ff0000", "bright red")
    print(c.get_name())
    c.set_name("red")
    print(c.get_name())



#################  Python's response

class PyColor:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name


def main2():
    c = PyColor("#ff0000", "bright red")
    print(c.name)
    c.name = "red"
    print(c.name)


#############  Java's argument

# We need more sophisticated methods to access attributes

class JavaColor(Color):
    def set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name


# [You have to make public attributes go private.
# The reason you have to do this is that you
# set more rigorous procedures to set/change
# the value of attributes, therefore direct
# access is not allowed anymore.]

# Then all the codes doing direct access suffers
# breaking down.

# Then java's mantra is that you should never
# let public attribute go private


################ python's counterattack

################# the property keyword


class NewColor:
    def __init__(self, rgb_value, name):
        self.rgb_value= rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name) # does the order of args matters?



def main3():
    c = NewColor("#0000ff", "bright red")
    print(c.name)
    c.name = "red"
    print(c.name)
    try:
        c.name = ""
    except Exception as e:
        print(e)


############## details of property


class Silly:
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoa, you killed silly!")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property.")
    # if the last argument not included, the help will return the doc of first argument
    # i.e., the _get_silly method in our example

################## use decorator to realize property

# This is not about the mechanism of decorators
# For that, refer to oo10

class Silly:
    @property
    def silly(self):   # decorator provides no docstring arg,
        "This is a silly property."   # provides the docstring in getter method
        return self._silly
    # This applies the property function as a decorator,
    # which is equivalent to the silly=property(silly) syntax.

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value
    # The property function returns an object with setter attibute
    # which can be the decorator of other functions.

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly


def main4():
    s = Silly()
    # It is your business to do dangerous things like s._silly = "foo"
    s.silly = "funny"
    s.silly
    del s.silly # compare it with del s
    help(s) # see what is reported and what is not in help

################### when to use properties

# caching values for calculations that are expensive

from urllib.request import urlopen

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):   # this is the getter
        if not self._content:
            print("Retrieving new page...")
            self._content = urlopen(self.url).read()
        return self._content

def main5():
    import time
    webpage = WebPage("http://ccphillips.net/")
    now = time.time()
    content1 = webpage.content
    print(time.time() - now)
    now = time.time()
    content2 = webpage.content
    print(time.time() - now)
    print(content2 == content1)

# the following property is set like this
# since we can calculate it on a fly.


class AverageList(list):
    @property
    def average(self):
        return sum(self)/len(self)

def main6():
    import time
    a = AverageList([1, 2, 3, 4])
    now = time.time()
    a.average
    print(time.time() - now)
    now = time.time()
    a.average
    print(time.time() - now)


if __name__ == "__main__":
    main4()