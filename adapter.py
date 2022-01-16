class User:
    def __init__(self, username, is_admin):
        self.username = username
        self.is_admin = is_admin

class Operator:
    def __init__(self, id, user):
        self.id = id
        self.user = user

class System:
    def __init__(self, operator):
        self.operator = operator
    
    def config(self):
        if self.operator.user.is_admin == True :
            print('You are allowed to config the system...')
        else:
            print("You aren't allowed to config the system...")

######################################

u1 = User('cha552',True)
o1 = Operator('10',u1)
sys1 = System(o1)

o1.config()


