# sets are unordered

# in python, set can hold any hashable objects
# so lists and dictionaries are out


song_library =[('a', 1), ('b', 1), ('c', 2), ('d', 3)]

artists = set()

for song, artist in song_library:
    artists.add(artist)

artists

# There is no built-in syntax for empty set
# but we can use curly braces
# compare:

{'a', 'b'}
{'a':'b'}