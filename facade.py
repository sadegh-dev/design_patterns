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
