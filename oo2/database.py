class Query:
    pass

class Second:
    pass


class Database:
    pass

db = Database()

# delay creating database when db1 is imported
# in other module

db1 = None

def initialize_database():
    global db1
    db1 = Database()




