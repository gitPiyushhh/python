# ############################################
# ####### 1. SINGLY LINKED LIST

# ## Creation

# # Initialisation of the node 
# from os import remove


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# node1 = Node(10)

# # Initialisation of the Linked List 

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def print_LL(self):
#         if self.head is None:
#             print ("LL is empty")
        
#         else:
#             n = self.head  # 'Just to make name small'
            
#             while n is not None:
#                 print(n.data)
#                 n = n.ref
            
#     def add_begin(self, data):
#         # Create node 
#         new_node = Node(data)

#         # Add the reference
#         new_node.ref = self.head

#         # Add the new refersnce
#         self.head = new_node

#     def add_end(self, data):
#         # Create node 
#         new_node = Node(data)

#         # Check if LL is empty
#         if self.head is None:
#             self.head = new_node

#         # Add the reference of current end node to new node
#         n = self.head

#         while n.ref is not None:
#             n = n.ref  #This loop is to move to the last node
#         n.ref = new_node

#     def add_between(self, data, x):
#         # New node
#         new_node = Node(data)

#         # Check for the node after which  we need to insert
#         n = self.head

#         while n is not None:
#             if n.data == x:
#                 break
#             else:
#                 n = n.ref 
        
#         if n is None: print("Node not present")
#         else:
#             new_node.ref = n.ref
#             n.ref = new_node

#     def add_empty(self, data):
#         if self.head is None:
#             new_node = Node(data)

#             self.head = new_node

#         else:
#             print("Node already present")

#     def remove_begin(self):
#         if self.head is None:
#             print("Empty LL")
#         else:
#             self.head = self.head.ref
    
#     def remove_end(self):
#         n = self.head

#         if n is None:
#             print("Empty LL")
        
#         elif n.ref is None:
#             n.ref = None 

#         while n.ref.ref is not None:
#             n = n.ref
        
#         n.ref = None

#         ## In detail 🙂
#         # # Traverse the whole LL
#         # while self.head.ref.ref is not None:
#         #     self.head = self.head.ref

#         # #Make the reference of second last node as None
#         # self.head.ref = None

#     def remove_by_value(self, data):
#         n = self.head

#         if n is None:
#             print('Empty LL')
        
#         else:
#             # If first node
#             if n.ref is None:
#                 self.remove_begin()

#             # If between node

#             else:
#                 while n.data == data:
#                     n = n.ref
                
#                 n.ref = n.ref.ref

#             # # Last node
#             # self.remove_end()

            
        


    
# lst1 = LinkedList()
# lst2 = LinkedList()

# ## Insertion
# lst1.add_begin(10)
# lst1.add_end(20)
# lst1.add_end(30)
# lst1.add_between(25, 20)

# lst2.add_empty(1)

# ## Traversal
# lst1.print_LL()
# lst2.print_LL()

# ## Deletion
# lst1.remove_begin()
# lst1.remove_end()
# lst1.remove_by_value(25)
# lst1.remove_by_value(20)

#################################################
############## DOUBLY LINKED LISTS 

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_end(self, data):
        new_node = Node(data)
        n = self.head

        if n is None:
            n = new_node
        

        while n.next is not None:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def traverse(self):
        n = self.head

        while n is not None:
            print(n.data)
            n = n.next


dll = DoublyLinkedList()

dll.add_end(1)
dll.add_end(2)
dll.add_end(3)
dll.traverse()