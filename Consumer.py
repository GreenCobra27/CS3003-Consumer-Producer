import random
import queue

# Creating the queue
queue = []

class Producer:
    #constructor
    def __init__(self, ID, Min, Max):
        self.ID = ID
        self.Min = Min
        self.Max = Max
    def generate(self):
        x = random.randint(self.Min, self.Max)
        return x
        
class Consumer:
    #constructor
    def __init__(self):
        self.tally = 0
    def consume(self):
        self.tally = self.tally + 1
        print('*' * 35)
        print('The tally amount is ' + str(self.tally))
        print('The id of the produced item is ' + str(queue[0].ID))
        print('*' * 35)
        queue.pop(0)
        
# Main function
p1 = Producer(1, 5, 90)
p2 = Producer(2, 10, 90)
p3 = Producer(3, 50, 150)
queue.append(p1)
queue.append(p2)
queue.append(p3)
c = Consumer()
c.consume()
c.consume()
