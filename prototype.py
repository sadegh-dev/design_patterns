from copy import deepcopy

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
class Prototype:
    def __inint__(self):
        self._objects = {}
    
    def register(self, ip, obj):
        self._objects[ip] = obj
    
    def unregister(self, ip):
        del self._objects[ip]

    def clone(self, ip, **kwargs):
        clonedObj = deepcopy(self._objects.get(ip))
        clonedObj.__dict__.update(kwargs)
        return clonedObj

serv1 = Server('102.203.605.300','4040')

# Copy Server details

storage = Prototype()

storage.register('100.200.300.400', serv1)
serv2 = storage.clone('100.200.300.400')

storage.register('101.202.303.404', serv1)
serv3 = storage.clone('101.202.303.404', ip='5060')

# whow data storage

print( serv1.__dict__ )
print( serv2.__dict__ )
print( serv3.__dict__ )