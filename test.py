## Fill it🙂

# A = [8, 3, 9, 8]
# B = [2, 4, 6, 5]

# temp_sum = 0

# for i in range(1, len(A)):
#     sum = A[i] + B[i] + A[i-1] + B[i-1]
#     if sum > temp_sum:
#         temp_sum = sum


# print(temp_sum)


# def minOperations(N, K, arr):
#     cnt = 0

#     test = set(arr)

#     if len(test) == 1: return 1

#     if len(test) < len(arr):
#         cnt = len(test) - 1

#     else: cnt = len(test) / K + len(test) % K

#     return int(cnt)



# # arr = [1, 1]
# # arr = [2, 1]
# arr = [1, 1, 5, 1, 1, 2, 4]
# k = 2

# print(minOperations(5, 2, arr))

# def equilibriumPoint(A, N):
#     mid = int(N / 2)
        
#     left = 0
#     right = 0
        
#     while mid > 0 and mid < N-1:
#         for i in range(0, mid):
#             left += A[i]
                
#         for i in range(mid+1, N):
#             right += A[i]
            
#         if left == right: return mid+1
#         else:
#             if left > right: mid = mid -1 
#             else: mid = mid +1 
            
            
            
# def equilibriumPoint(A, N):
#     for i in range(0, N-2):
#         for j in range(i+1, N):
#             if A[j] > A[i]: return
#         print(arr[i], end = ' ')
#     print(arr[-1])

# arr = [1, 1, 1, 1, 2, 5, 3, 3]

# equilibriumPoint(arr, 8)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def print__ll(self):
        if self.head:
            while self.head:
                print(self.head.data)
                self.head = self.head.next
        else: print('Empty LL')
    
    def insert_start(self, data):
        new_node = Node(data)
        # 1. Make the new head ref
        new_node.next = self.head
        # 2. Make new head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        # 1. Traverse to the last node
        
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def insert_middle(self, data):
        node = Node(data)
        head = self.head

        # 1. Counter create
        count = 0
        
        # 2. Traverse the whole ll and update len in counter
        n = head
        while n.next is not None:
            n = n.next
            count += 1
        
        print(count)
        # 3. Traverse to len/2 
        target = int(count / 2)
        
        # 4. Traverse to target
        print(target)
        n = head
        
        while target != 0:
            n = n.next
            target -= 1
        
        # Insert new node
        
        node.next = n.next
        n.next = node

    
ll = LinkedList()
ll.insert_start(10)
ll.insert_end(40)
ll.insert_middle(30)
# ll.print__ll()