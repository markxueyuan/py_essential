# Do Lists in python have mutable/immutable data structures?

names = ["Dave", "Mark", "Ann", "Phil"]

a = names[2]  # return the third item
print(a)

names[0] = "Jeff"  # change the first item
print(names)

names.append("Paula")
print(names)

names.insert(2, "Thomas")  # insert into the third slot
print(names)

b = names[0:2]
c = names[2:]
print("b is ", b)
print("c is ", c)
names[3] = 'Jeff'  # replace the second
names[0:2] = ["Dave", "Mark", "Jeff"]  # replace the first two item with the list
print(names)
a = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
print(a[3][3][1])  # applying indexing operation multiple times

# concatenate

a = [1, 2, 3] + [4, 5]
print(a)

# empty lists

ep = []
ep2 = list()

# nested list

a = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
print(a[3][3][1])  # applying indexing operation multiple times




