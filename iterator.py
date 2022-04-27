class iterator:
    
    def __init__(self, index, step):
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
    def __init__(self, up, step=1):
        self.up = up
        self.step = step
    
    def __iter__(self):
        return iterator(self.up, self.step)


f1 = CustomCounter(9)
f2 = iter(f1)
print(next(f2))
print(next(f2))
print(next(f2))

