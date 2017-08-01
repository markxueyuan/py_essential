# open() built-in is used to open a file and return a file object

# the bytes will be converted to text using the platform default encoding

contents = "some contents"
file = open("atext", 'w') # 'w' is called a mode argument
file.write(contents)
file.close()


# 'a' is the mode argument for append

# to open a binary file, use mode string 'b', so 'rb' to read, 'wb' to write
# such files

# when we read such a file, it will return byte objects instead of str

f = open("atext", 'r')
f.read()
g = open('atext', 'rb')
g.read()
x = open('atext')
x.read()

u = open("atext", 'a')
u.write("\nWe just need more lines")
u.close()
r = open("atext")

for l in r:
    print(l)
r.close()

r = open("atext")
r.readlines()

r = open("atext", 'a')
r.writelines(['a', 'b', 'c'])
# writelines is a poorly named function, it doesn't add \n at the end.
r.close()
r = open("atext")
r.read()
r.close()