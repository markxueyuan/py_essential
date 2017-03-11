import random

a = random.randint(0, 100)
b = random.randint(0, 100)


if a < b:
    print("Computer says Yes")
else:
    print("Computer says No")

if a < b:
    pass  # do nothing
else:
    print("Computer says No Again")

##
product = "game"; type = "private memory"
age = random.randint(0, 15)

if product == "game" and type == "private memory" \
    and not (age < 4 or age > 8):
    print("I will take it!")
else:
    print("I will not!")

##

suf = [".htm", ".jpg", ".png", "hehe"]
suffix = random.choice(suf)
if suffix == ".htm":
    content = "text/html"
elif suffix == ".jpg":
    content = "image/jpeg"
elif suffix == ".png":
    content = "image/png"
else:
    raise RuntimeError("Unknown content type")
print(content)

##

x = ['spam']; y = ['']
s = random.choice([x, y])
if 'spam' in s:
    has_spam = True
else:
    has_spam = False
print(has_spam)

# or
has_spam = 'spam' in s
print("or: ", has_spam)

# The in operator is commonly used to check if
# a value is contained inside of another object


# random.choice is quite convenient to use


