class iterator:
    
    def __init__(self, index, step=1):
        self.index = index
        self.step = step
    
    def __next__(self):
        if self.index == 0 :
            return None
        for x in range(0, self.index, -self.step ):
            pass



class CustomCounter:
    def __init__(self, up, step):
        self.up = up
        self.step = step
    
    def __iter__(self):
        pass