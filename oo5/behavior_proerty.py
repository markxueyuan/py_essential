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



if __name__ == "__main__":
    main3()