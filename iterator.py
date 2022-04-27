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


# Example 1
f1 = CustomCounter(9)
f2 = iter(f1)
print(next(f2))
print(next(f2))
print(next(f2))


# Example 2

e1 = CustomCounter(12,3)
e2 = iter(e1)
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))
print(next(e2))
