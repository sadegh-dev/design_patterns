from abc import ABC, abstractmethod

# Creator --------------- #

class Connect(ABC):
    @abstractmethod
    def the_type(self):
        pass

    def call_create(self):
        db = self.the_type()
        table = db.create_()
        return table

class Sql(Connect):
    def the_type(self):
        return Postgresql()

class Nosql(Connect):
    def the_type(self):
        return Mongodb()


# Product --------------- #

class Database(ABC):
    @abstractmethod
    def create_(self):
        pass

class Postgresql(Database):
    def create_(self):
        return 'Create Postgresql Database'

class Mongodb(Database):
    def create_(self):
        return 'Create Mongodb Database'

# Client --------------- #

def project(db):
    return db.call_create()

#########################

print(project(Sql()))
print(project(Nosql()))
