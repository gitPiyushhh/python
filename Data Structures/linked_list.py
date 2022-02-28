############################################
####### 1. SINGLY LINKED LIST

## Creation

# Initialisation of the node 

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

node1 = Node(10)

print (node1)

# Initialisation of the Linked List 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print ("LL is empty")
        
        else:
            n = self.head  # 'Just to make name small'
            
            while n is not None:
                print(n.data)
                n = n.ref
    
lst1 = LinkedList()

lst1.print_LL()


## Insertion


## Traversal

# If LL is empty




## Deletion