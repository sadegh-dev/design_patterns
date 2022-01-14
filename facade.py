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


