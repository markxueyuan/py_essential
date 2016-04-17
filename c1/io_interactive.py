from sys import stdin, stdout

# The noted code doesn't work as I expected
# stdout.write("Enter your name :")
# name = stdin.readline()
# print("You just typed: ", name)

name = input("Enter your name: ")
stdout.write("You just typed: %s" % name)
