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

#