# sets are unordered

# in python, set can hold any hashable objects
# so lists and dictionaries are out


song_library =[('a', "James"), ('b', "Eric"), ('c', "John"), ('d', "Eric")]

artists = set()

for song, artist in song_library:
    artists.add(artist)

artists

# There is no built-in syntax for empty set
# but we can use curly braces
# compare:

{'a', 'b'}
{'a':'b'}

for artist in artists:
    print("{} plays good music".format(artist))

alphabetical = list(artists)
alphabetical.sort()
alphabetical


seta = {'a', 'b', 'c', 'd', 'e'}
setb = {'d', 'e', 'f', 'g', 'h'}

# symmetric operation

print("All: {}".format(seta.union(setb)))
print("Both: {}".format(seta.intersection(setb)))
print("Either but not both: {}".format(
    seta.symmetric_difference(setb)
))


setc = {'a', 'b', 'c'}

# asymmetric operation
setc.issubset(seta)

seta.issuperset(setc)
seta.difference(setb)
setb.difference(seta)


print("*"*20)


'a' in setc

# Sets are much more efficient than lists when
# checking for membership using the in keyword

# for set, it simply hashes the value and checks
# for membership

# This means that a set will find the value in
# the same amount of time no matter how big the
# container is



