class iterator:
    
    def __init__(self, index, step=1):
        self.index = index
        self.step = step
    
    def __next__(self):
        if self.index == 0 :
            return None
        
        while self.index > 0 :
            now_index = self.index
            self.index -= self.step
            return now_index


class CustomCounter:
    def __init__(self, up, step):
        self.up = up
        self.step = step
    
    def __iter__(self):
        pass




