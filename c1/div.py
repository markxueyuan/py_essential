def divide(a, b):
    q = a // b  # // returns the quotient
    r = a - q * b
    return (q, r)

def te():
    print("say teeee")

print(divide(5,3))
