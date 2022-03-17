# # ## Fill it🙂

# # # A = [8, 3, 9, 8]
# # # B = [2, 4, 6, 5]

# # # temp_sum = 0

# # # for i in range(1, len(A)):
# # #     sum = A[i] + B[i] + A[i-1] + B[i-1]
# # #     if sum > temp_sum:
# # #         temp_sum = sum


# # # print(temp_sum)


# # # def minOperations(N, K, arr):
# # #     cnt = 0

# # #     test = set(arr)

# # #     if len(test) == 1: return 1

# # #     if len(test) < len(arr):
# # #         cnt = len(test) - 1

# # #     else: cnt = len(test) / K + len(test) % K

# # #     return int(cnt)



# # # # arr = [1, 1]
# # # # arr = [2, 1]
# # # arr = [1, 1, 5, 1, 1, 2, 4]
# # # k = 2

# # # print(minOperations(5, 2, arr))

# # # def equilibriumPoint(A, N):
# # #     mid = int(N / 2)
        
# # #     left = 0
# # #     right = 0
        
# # #     while mid > 0 and mid < N-1:
# # #         for i in range(0, mid):
# # #             left += A[i]
                
# # #         for i in range(mid+1, N):
# # #             right += A[i]
            
# # #         if left == right: return mid+1
# # #         else:
# # #             if left > right: mid = mid -1 
# # #             else: mid = mid +1 
            
            
            
# # # def equilibriumPoint(A, N):
# # #     for i in range(0, N-2):
# # #         for j in range(i+1, N):
# # #             if A[j] > A[i]: return
# # #         print(arr[i], end = ' ')
# # #     print(arr[-1])

# # # arr = [1, 1, 1, 1, 2, 5, 3, 3]

# # # equilibriumPoint(arr, 8)

# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
    
# # class LinkedList:
# #     def __init__(self):
# #         self.head = None

# #     def print__ll(self):
# #         if self.head:
# #             while self.head:
# #                 print(self.head.data)
# #                 self.head = self.head.next
# #         else: print('Empty LL')
    
# #     def insert_start(self, data):
# #         new_node = Node(data)
# #         # 1. Make the new head ref
# #         new_node.next = self.head
# #         # 2. Make new head
# #         self.head = new_node

# #     def insert_end(self, data):
# #         new_node = Node(data)

# #         if self.head is None:
# #             self.head = new_node

# #         # 1. Traverse to the last node
        
# #         else:
# #             n = self.head
# #             while n.next is not None:
# #                 n = n.next
# #             n.next = new_node

# #     def insert_middle(self, data):
# #         node = Node(data)
# #         head = self.head

# #         # 1. Counter create
# #         count = 0
        
# #         # 2. Traverse the whole ll and update len in counter
# #         n = head
# #         while n.next is not None:
# #             n = n.next
# #             count += 1
        
# #         # 3. Traverse to len/2 
# #         target = int(count / 2)
        
# #         # 4. Traverse to target
# #         print(target)
# #         n = head
        
# #         while target != 0:
# #             n = n.next
# #             target -= 1
        
# #         # Insert new node
        
# #         node.next = n.next
# #         n.next = node

# #     def rotate(self, k):
        
# #         # 1. Traverse to the kth node
# #         head = self.head
        
# #         old_head = head
        
# #         for i in range(1, k):
# #             head = head.next  # now head is pointing to the kth node ka head
        
        
# #         ptr = head
        
# #         while ptr.next is not None:
# #             ptr = ptr.next
        
# #         ptr.next = old_head 

# #         while old_head != ptr:
# #             old_head = old_head.next
        
# #         old_head.next = None
        
# #         return head

    
# # ll = LinkedList()
# # ll.insert_start(10)
# # ll.insert_end(40)
# # ll.insert_middle(30)
# # # ll.rotate(1)
# # ll.print__ll()

# # ll2 = LinkedList()

# # ll2.insert_end(1)
# # ll2.insert_end(2)
# # ll2.insert_end(3)
# # ll2.insert_end(4)
# # ll2.insert_end(5)
# # ll2.insert_end(6)
# # ll2.insert_end(7)
# # ll2.insert_end(8)

# # ll2.rotate(4)
# # ll2.print__ll()


# #User function Template for python3


# class Solution:
#     def nsel_calc(self, arr, n):
#         ans = []
#         stk = []
        
#         for i in range(n):
#             while len(stk) != 0 and stk[-1][0] >= arr[i]: stk.pop()
            
#             # No smaller element
#             if len(stk) == 0: ans.append(-1)
            
#             else: ans.append(stk[-1][1])
            
#             stk.append([arr[i], i])
        
#         return ans
    
#     def nser_calc(self, arr, n):
        
#         stk = []
#         ans = []
        
#         for i in range(n-1, -1, -1):
#             # Here we run neg loop kyuki to right nikalna h seedha loop chalega toh left elems store hoge🙂4
#             while len(stk) != 0 and stk[-1][0] >= arr[i]:
#                 # Elem smaller h nikal k fek do
#                 stk.pop()
            
#             if len(stk) == 0: ans.append(-1)
            
#             else: ans.append(stk[-1][1])
            
#             stk.append([arr[i], i])
            
#         ans.reverse()
        
#         return ans
        
#     #Function to find largest rectangular area possible in a given histogram.
#     def getMaxArea(self,h):
#         # Next smaller element on the left
#         nsel = self.nsel_calc(h, len(h))
#         # Next smaller element on the right
#         nser = self.nser_calc(h, len(h))
        
        
#         area = []
#         max_area = 0
#         test = h
#         test2 = h
        
#         flag = False

#         test.sort()
#         test2.sort(reverse=True)
        
#         if test.sort() == h or test2.sort(reverse = True) == h: flag = True
        

#         print(flag)
        
#         for i in range(n):
        
#             if not flag: width = nser[i] - nsel[i] - 1 #As the nser index is greater as on right
#             # When we have no right smaller elem
#             else: width = n-i
#             height = h[i]
#             area = width * height
            
#             if area > max_area: max_area = area
        
#         return max_area
        
    
# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# # by Jinay Shah 

# if __name__ == '__main__':
#     test_cases = 1
#     for cases in range(test_cases) :
#         n = 5
#         a = [5, 4, 3, 2, 1]
#         ob=Solution()
#         print(ob.getMaxArea(a))

from queue import Queue


q = Queue()

print(q.append(1))
print(q.append(2))
print(q.append(3))

print(q.getFront())