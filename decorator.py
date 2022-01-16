def admin(func):
    def check_admin():
        user = input('Enter username: ')
        if user == 'admin' :
            func()
        else:
            print('You do not have permission to run this function.')
    return check_admin

####################

@admin
def work():
    print('work function ir RUN.')

####################

work()
