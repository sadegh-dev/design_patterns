# ######## Facade ######## #
class Monitoring():
    def __init__(self):
        print(":: Welcome to monitoring ::")

    def statistics(self):
        self.user = MyUser()
        self.viewer = Viewer()
        self.transaction = Transaction()

        self.user.newusers()
        self.viewer.popularpages()
        self.transaction.most()


# ######## Subsystems ######## #
class MyUser():
    def __init__(self):
        print("create new object of MyUser")
    
    def newusers(self):
        print("These are the newest users : Charlie , John")


class Viewer():
    def __init__(self):
        print("create new object of Viewer")
    
    def popularpages(self):
        print("These are the popular pages : home , category")


class Transaction():
    def __init__(self):
        print("create new object of Transaction")
    
    def most(self):
        print("These are the most transaction : Buy Book , Send Email")
