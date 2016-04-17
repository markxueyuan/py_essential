# What is stack? (https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29)
# What is the first argument of each method?
# What is the difference between instance method and static method?

items = [37, 42]  # set up an object
items.append(73)  # edit the object

print(dir(items))  # dir lists all methods available on the object

print(items.__repr__())  # double underscore method
print(items.__str__())
print(items.__add__([99, 66]))

# build new class


class Stack(object):     # Stack inherits from object, the root of all python types
    def __init__(self):  # initialize a stack
        self.stack = []

    def push(self, object):
        self.stack.append(object)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)

    def __str__(self):
        #  make common functions like print, str work in the Stack
        return str(self.stack)


s = Stack()  # create a stack
s.push("Dave")  # push into a stack
s.push(42)
s.push([3, 4, 5])
print(s)
x = s.pop()
print("x is", x)
print("s is", s)
del s

# inherit from list


class Stack(list):  # Stack inherit from list
    def push(self, object):
        self.append(object)
    # since Stack inherit from list, it can use any methods of list
        # to build its own method

    @staticmethod  # declare as static method
    def privateStack():
        # This static method returns a stack containing an element "Treasure"
        s = Stack()
        s.push("Treasure")
        print(s)
        return s

Stack.privateStack()  # call a static method



