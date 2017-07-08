from oo3.extend_builtin import Contact

class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

# Friend now inherit from Contact and AddressHolder.
# In multiple inheritance, we now have two parent __init__ method


# A naive approach

class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone


# [Notice that different from super(), here we need to explicitly let
#  the methods of the parents know on which objects it works on]

# The naive approach has some problems:

# 1. Possibly uninitialize a superclass because of neglect, causing hard to
# debug problems

# 2. More sinister, the superclass is initialized twice.

############## Method Resolution Order

## Which is beyond the scope of the book.



################ Second example for diamond inheritance


# we get the name because this type of inheritance gets a shape of diamond.

class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on base class.")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on left subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on right subclass")
        self.num_right_calls += 1

class SubClass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on subclass")
        self.num_sub_calls += 1


def main():
    s = SubClass()
    s.call_me()
    print(s.num_sub_calls, s.num_left_calls,
          s.num_right_calls, s.num_base_calls)

# funny to realize that you can `call' all static variable
# of the parent or ancestor class directly on the object


if __name__ == "__main__":
    main()

# super was originally developed to make complicated forms of multiple
# inheritance possible


################### the improvement

class BaseClass2:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on base class")
        self.num_base_calls += 1

class LeftSubclass2(BaseClass2):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on left subclass")
        self.num_left_calls += 1

class RightSubclass2(BaseClass2):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on right subclass")
        self.num_right_calls += 1


class SubClass2(LeftSubclass2, RightSubclass2):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()   # surprisingly
        print("Calling method on subclass")
        self.num_sub_calls += 1



def main2():
    s = SubClass2()
    s.call_me()
    print(s.num_sub_calls, s.num_left_calls,
          s.num_right_calls, s.num_base_calls)

# funny to realize that you can `call' all static variable
# of the parent or ancestor class directly on the object


if __name__ == "__main__":
    main2()

# the improvement comes from the realization of calling
# the next method in the class hierarchy, instead of
# the parent method.