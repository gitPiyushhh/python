######################################
#### Creation {Using list}

import collections
from numpy import stack


stk = []

## Adding elements
stk.append(1)
stk.append(2)
stk.append(3)

## Removal
print(stk.pop())
print(stk.pop())
print(stk.pop())

## Empty or not
print(len(stk) == 0) ## Empty for now🙂
print(not stk) ## Empty for now🙂

#######################################
##### Creation {Using deque}

stk = collections.deque()
print(stk)

## Adding elements
stk.append(1)
stk.append(2)
stk.append(3)

## Removal
print(stk.pop())
print(stk.pop())
print(stk.pop())


###################################################
########## Implementation through Linked List😌

class StackNode:
    def __init__(self, data):
        self.data = data
    
class MyStack:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        ## 1. Node creation
        new_node = StackNode(data)

        ## 2. Node insertion  on the top
        new_node.next = self.root

        self.root = new_node

        return
    
    def remove(self):
        ## 1. Make the next node first node
        r = self.root

        if r is None:
            return -1

        self.root = self.root.next 

        return r.data

stk = MyStack()

stk.insert(1)
stk.insert(2)

print(stk)

last = stk.remove()
sec_last = stk.remove()
third_last = stk.remove()
print(last, sec_last, third_last)