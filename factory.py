from abc import ABC, abstractmethod



# Product
class Database(ABC):
    @abstractmethod
    def __init__(self, db_name, username, password):
        pass

class Postgresql(Database):
    def __init__(self, db_name, username, password):
        pass

