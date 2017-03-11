from sys import stdin, stdout

# The anormaly unexplained
#stdout.write("Enter your name :")
#name = stdin.readline()
#print("")
#print("You just typed: ", name)

# alternatively
name = input("Enter your name: ")
stdout.write("You just typed: %s" % name)
print("")
