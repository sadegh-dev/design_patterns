class iterator:
    
    def __init__(self, index, step):
        self.index = index
        self.step = step
    
    def __next__(self):
        if self.index == 0 :
            return None






class CustomCounter:
    def __init__(self, up, step):
        self.up = up
        self.step = step
    
    def __iter__(self):
        pass