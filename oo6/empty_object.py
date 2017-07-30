# Since every other class will inherit from object, object cannot be freely
# assigned an attribute, for the sake of economy.

o = object()


try:
    o.x = 5
except AttributeError as e:
    print(e)


