p1 = Person('charlie', '123456')
c1 = Car('456321',p1)
g1 = Garage(c1)

g1.exitـpermission()
##############################3
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

p1 = 


