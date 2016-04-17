# Why need to catch the error?

# Why f.close() is not needed anymore when using with statement?

try:  # try
    raise RuntimeError("Computer says no")  # throw an error
except RuntimeError as e:  # catch the error
    print(e)

# with statement


with open("demo3.txt", "a") as f:
    # a represents file opened in appendable mode
    f.write("You can see me at last line.\n")

with open("demo3.txt", "r") as f:
    # r represents file opened in readable mode
    print(f.readlines())






