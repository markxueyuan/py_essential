# pure paths provide purely computational operations without i/o
# concrete paths inherit from pure paths but provide i/o
# If to manipulate Windows paths on a Unix machine, cannot instantiate
# a WindowsPath on Unix, but can instantiate PureWindowsPath

################# Basic Uses


from pathlib import Path, PurePath, PureWindowsPath, WindowsPath

p = Path(".")

[x for x in p.iterdir() if x.is_dir()]

list(p.glob('**/*.py'))

# Although use Path, it instantiates a PosixPath

p = Path("/media/markxueyuan/Data")

# Navigate inside a directory tree
q = p / 'pdf'

q.resolve() # seems to show the original directory

# query path properties
q.exists()
q.is_dir()

d = Path(".").resolve()
t = d / "oo5" / "text.txt"

with t.open() as f:
    print(f.readline())

######################## Pure paths

# PurePath is a generic class representing the system's path flavour
# Creates either a PurePosixPath or PureWindowsPath

PurePath('setup.py')

# PurePath receives arguments string, bytes objects or another path object

PurePath('foo', 'some/path', 'bar')
PurePath(Path('foo'), Path('bar'))
PurePath()
Path()

##### Well, I am not patient to type them all. Read the doc if necessary

########## getting the operating system's name

import os
os.name
os.getcwd() # which is in essence the same as
Path.cwd()