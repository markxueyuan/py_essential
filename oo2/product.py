## Variations of import

##

import oo2.database as db

db = db.Database()

# namespace: the list of names currently
# accessible in a module or function

##

from oo2.database import Database

db = Database()

## rename class in the current namespace

from oo2.database import Database as DB

db = DB()

## import multiple classes

from oo2.database import Query, Database

query = Query()
db = Database()

## import all classes and functions

from oo2.database import *

# Reason toavoid this syntax is
# for you may need tounderstand your code two years late


class Product:
    pass


