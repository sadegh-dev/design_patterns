class ConnectToDb:
    def __init__(self):
        print('Connect to database ...')


class Proxy :
    def check_admin(self,is_admin):
        if is_admin :
            c1 = ConnectToDb()
            return c1
        else :
            return None

