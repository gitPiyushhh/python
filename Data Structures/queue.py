#########################################
####### Creation {using list}
import sys


q = []

## Adding elements
q.append(1)
q.append(2)
q.append(3)

## Retrieval of elements
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

#########################################
####### Creation {using circular array}🙂

class Queue:
    SIZE = 10
    queue = [-sys.maxsize - 1] * 10 

    def __init__(self):
        self.front = -1
        self.rear = -1
    
    def is_full(self):
        f = self.front
        r = self.rear
        if f == 0 and r == self.SIZE - 1:
            return True
        if f == r + 1:
            return True
        return False
    
    def is_empty(self):
        if self.front == -1:
            return True
        return False
        

    ## 1. Enque Operation
    def enque(self, data):
        
        if self.is_full():
            print('Queue is full')
        
        else:
            if self.front == -1:
                self.front = 0 # Increment f only once
            
            self.rear = (self.rear + 1) % self.SIZE  # Circular array rotation
            self.queue[self.rear] = data # append data
            print("Operation successful🙂, rear at ", data)
    

    def deque(self):
        if self.is_empty():
            print('Queue is empty')
            return -1

        else:
            elem = self.queue[self.front]

            # If only one elem presnt then return it and reset queue
            if self.front == self.rear:
                self.front , self.rear = -1

            else:
                self.front = (self.front + 1) % self.SIZE

            return elem  



q = Queue()

q.enque(1)
q.enque(2)
q.enque(3)
q.deque()
delet = q.deque()
print(delet)