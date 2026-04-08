import random 

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.label = self._get_label() 
    
    def _get_label(self):
        return 1 if self.x > self.y else -1
    
    def debug(self):
        print(f"Label: {self.label}\tx: {self.x}\ty: {self.y}")
    
