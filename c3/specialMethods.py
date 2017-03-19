# special methods map non-method-calling syntax into method calls

# 1. __init__ is not a constructor, __init__ is immediately called
# after the instance has already been created.
# __init__ provides the syntax that makes the class callable.

# 2. __getitem__ provides the [] lookup syntax

# 3. __setitem__ provides the a[key] = val set syntax



from collections import UserDict

# object creation and destruction


class A(object):
    _dict = dict()

    def __new__(cls):
        if 'key' in A._dict:
            print("Exists")
            return A._dict['key']
        else:
            print("New")
            return super(A, cls).__new__(cls)

    def __init__(self):
        print("Init")
        A._dict['key'] = self
        print("")


class Loaf:
    pass


def stripnulls(data):
    """strip whitespace and nulls"""
    return data.replace("\00", "").strip()


class FileInfo(UserDict):
    """store file metadata"""
    def __init__(self, filename=None):  # the init method never returns a value
        UserDict.__init__(self)  # init the instance of ancestor class
        self["name"] = filename  # the object of UserDict acts like a dictionary

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, item):
        self.data[key] = item


class MP3FileInfo(FileInfo):
    """store ID3v1.0 MP3 tags"""
    tagDataMap = {"title": (3, 33, stripnulls),
                  "artist": (33, 63, stripnulls),
                  "album": (63, 93, stripnulls),
                  "year": (93, 97, stripnulls),
                  "comment": (97, 126, stripnulls),
                  "genre": (127, 128, ord)}

    def __setitem__(self, key, item):
        if key == "item" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)

    def __parse(self, filename):
        """parse ID3v1.0 tags from MP3 file"""
        self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            print("Fuck")

    def parse(self, filename):
        """parse ID3v1.0 tags from MP3 file"""
        self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-2256, 2)
                tagdata = fsock.read(2256)
            finally:
                fsock.close()
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
            else:
                print(tagdata)
        except IOError:
            print("Fuck")


class Counter:
    count = 0

    def __init__(self):
        self.__class__.count += 1







#  when call the method of an ancestor class from within the class,
# you must include the self argument; when call the method from outside,
# python automatically adds the python reference for you.

f = FileInfo("c3/red_rose.mp3")
print(f.__class__)
print(f.__doc__)
print(f)
print(f['name'])
f["genre"] = 32
print(f)

mp3file = MP3FileInfo()
print(mp3file)
mp3file.parse("c3/red_rose.mp3")
# mp3file["item"] = "red_rose.mp3"
print(mp3file)
print(MP3FileInfo)
print(MP3FileInfo.tagDataMap)
print(mp3file.tagDataMap)



print(Counter)
print(Counter.count)
c = Counter()
print(c.count)
print(Counter.count)
d = Counter()
print(d.count)
print(c.count)
print(Counter.count)




################ garbage collection

# the local variable f goes out of scope, there are no reference to the
# newly created file, therefore they will be garbage collected


def leakmem():
    f = FileInfo(UserDict)

for i in range(100):
    leakmem()








