from oo3.extend_builtin import Contact

# overriding is a method to modify the inherited methods


# the (special) method __init is overridden. Still, all
# methods can be overriden

class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# However to avoid duplicates and make maintenance tractable
# We need to execute the original method first. This is how
# super works.

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

# It gets the instance of the parent object using super,
# calls __init__ on the object, passing in the expected arguments.
# [Then it does new things on this object]



