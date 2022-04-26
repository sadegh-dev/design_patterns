class ConnectToDb:
    def __init__(self):
        print('Connect to database ...')


class Proxy :
    def check_admin(self,is_admin):
        if is_admin :
            c1 = ConnectToDb()
            return c1
        else :
            print('Access Denied ..!')
            return None


connect1 = Proxy()

flag_admin = True
connect1.check_admin(flag_admin)

flag_admin = False
connect1.check_admin(flag_admin)