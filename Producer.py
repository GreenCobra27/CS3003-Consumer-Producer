import random

class Producer:

    #constructor
    def __init__(self, ID, Min, Max):
        self.ID = ID
        self.Min = Min
        self.Max = Max

    def generate(self):
        x = random.randint(self.Min, self.Max)
        return x
        
