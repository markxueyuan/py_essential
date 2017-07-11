# ABCs define a set of methods and properties that
# a class must implement in order to be considered a duck-type
# instance of that class

########## Use an abstract base class


# most ABCs live in the collections module

from collections import Container

def main():
    print(Container.__abstractmethods__) # get __contains__
    help(Container.__contains__) # get signature

if __name__ == "__main__":
    main()



class OddContainer:
    def __contains__(self, item):
        if not isinstance(item, int) or not item % 2:
            return False
        return True

oc = OddContainer()

def main2():
    print(isinstance(oc, Container))

if __name__ == "__main__":
    main2()


# Although OddContainer doesn't extend Container, the oc is a Container object

# That is why duck typing is more awesome than classical polymorphism


# The interesting about the Container ABC is that any class implements it
# gets to use the in keyword for free!!!!!!
# in is just the syntax sugar delegates to the __contains__ method


def main3():
    print(1 in oc)
    print(2 in oc)
    print(3 in oc)
    print(4 in oc)
    print("st" in oc)

if __name__ == "__main__":
    main3()


####################### Create an ABC


import abc

# Yi Bu Yi Wai, Jing Bu Jing Xi?

# Create an ABC to document what API the third-party plugins should provide


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass


    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod  # the method can be called on a class instead of an object
    def __subclasshook_(cls, C): # let interpreter answer, is C a subclass of this class?
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__)  <= attrs: # check if all the abstract methods have been supplied
                return True

        return NotImplemented # if nay of the conditions have not been met

class Wav(MediaLoader):
    pass

class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        pass

def main():
    try:
        x = Wav()
    except TypeError as e:
        print(e)

    o = Ogg()

if __name__ == "__main__":
    main()



# More common object-oriented languages have a clear separation between
# the interface and the implementation of a class.

# For example, some languages provide an explicit interface keyword that
# allows us to define the methods that a class must have without any
# implementation.

# In such an environment, an abstract class is one that provides both an
# interface and a concrete implementation of some but not all methods.
# Any class can explicitly state that it implements a given interface


# Python's ABCs help to supply the functionality of interfaces without
# compromising on the benefits of duck typing.



# Because of the __subclasshook__, we can use duck typing, no need for
# extending the MediaLoader class anymore.

class Ogg2():
    ext = ".ogg"
    def play(self):
        print("This will play an ogg file")


def main2():
    print(issubclass(Ogg, MediaLoader))
    print(isinstance(Ogg(), MediaLoader))


if __name__ == "__main__":
    main2()

