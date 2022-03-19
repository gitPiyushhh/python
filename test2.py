# # # # # # # # # ########################################
# # # # # # # # # ####### HASH MAP IMPLEMENTATION

# # # # # # # # # # prices = {
# # # # # # # # # #     '6Mar': 300,
# # # # # # # # # #     '7Mar': 400
# # # # # # # # # # }

# # # # # # # # # # print(prices.keys())
# # # # # # # # # # print(prices['6Mar'] + prices['7Mar'])

# # # # # # # # # stk = []

# # # # # # # # # s = 'aaabbccd'
        
# # # # # # # # # for i in s:
# # # # # # # # #     # Empty stk
# # # # # # # # #     if len(stk) == 0: 
# # # # # # # # #         stk.append(i)
# # # # # # # # #         continue
            
# # # # # # # # #     #For rest
# # # # # # # # #     if stk[-1] == i: 
# # # # # # # # #         print('Popped')
# # # # # # # # #         stk.pop(-1)
            
# # # # # # # # #     else: stk.append(i)
        
# # # # # # # # # print(stk)
        
# # # # # # # # # s = ''
# # # # # # # # # for i in range(len(stk)):
# # # # # # # # #     s += stk.pop(-1)
        

# # # # # # # # # stk = []
# # # # # # # # # s = 'abcde'

# # # # # # # # # for _ in s:
# # # # # # # # #     stk.append(_)

# # # # # # # # # print(stk)

# # # # # # # # # print(6//2)


# # # # # # # y, z= [int(i) for i in input().split()]
# # # # # # # col = [0] + [int(i) for i in input().split()]
# # # # # # # cutoff =[-1] + [-1 for i in range(y)]
# # # # # # # praj = set()
# # # # # # # l = []

# # # # # # # for i in range(z):
# # # # # # #   id, p, q, r, s = input().split(",")
# # # # # # #   id = int(id[8:])
# # # # # # #   p = float(p)
# # # # # # #   q = int(q[2:])
# # # # # # #   r = int(r[2:])
# # # # # # #   s = int(s[2:])
# # # # # # #   l.append([p, id, 1, q])
# # # # # # #   l.append([p, id, 2, r])
# # # # # # #   l.append([p, id, 3, s])
# # # # # # # l.sort(key = lambda x: (-x[0], x[1], x[2]))

# # # # # # # for i in l:
# # # # # # #   if i[1] not in praj:
# # # # # # #     if col[i[3]] > 0:
# # # # # # #       col[i[3]] -= 1
# # # # # # #       cutoff[i[3]] = i[0]
# # # # # # #       praj.add(i[1])

# # # # # # # col = [[col[i], i, cutoff[i]] for i in range(1, len(col))]
# # # # # # # col.sort(key = lambda x:(-x[0], x[1], x[2]))
# # # # # # # s = 0
# # # # # # # for i in l:
# # # # # # #   if i[1] not in praj:
# # # # # # #     while s < len(col) and col[s][0] <= 0:
# # # # # # #       s += 1
    
# # # # # # #     if s < len(col):
# # # # # # #       col[s][0] -= 1
      
# # # # # # #       if col[s][2] == -1:
# # # # # # #         col[s][2] = 100
      
# # # # # # #       col[s][2] = min(col[s][2], i[0])
      
# # # # # # #       praj.add(i[1])

# # # # # # # col.sort(key = lambda x: -x[2])
# # # # # # # for i in col:
# # # # # # #     if i[2]!=-1:
# # # # # # #         print("C"+str(i[1]),i[2])
# # # # # # #     else:
# # # # # # #         print("C"+str(i[1],"n/a"))           


# # # # # # # # def list_string(strn):
# # # # # # # #   level=[]
# # # # # # # #   def permute(prefix,suffix):
# # # # # # # #     level.append(prefix)
# # # # # # # #     if len(suffix)==0:
# # # # # # # #       return 
# # # # # # # #     for i in range(len(suffix)):
# # # # # # # #       permute(prefix,suffix[i], suffix[:i]+suffix[i+1:])
# # # # # # # #       permute("", strn)
# # # # # # # #       return level
    
# # # # # # # # t = []
# # # # # # # # t = list_string("hey")
# # # # # # # # v = int(input())
# # # # # # # # print(t[v])


# # # # # # def nsel(arr, n):
    	
# # # # # # 	nselIndex = []
# # # # # # 	s = []

# # # # # # 	for i in range(0, n):
# # # # # # 		while(len(s) != 0 and s[-1][0] <= arr[i]):
# # # # # # 			s.pop()

# # # # # # 		if len(s) == 0 :
# # # # # # 			nselIndex.append(-1)
# # # # # # 		else:
# # # # # # 			nselIndex.append(s[-1][1])

# # # # # # 		s.append([arr[i], i])
# # # # # # 	print(nselIndex)
# # # # # # 	return nselIndex


# # # # # # def nser(arr, n):
	
# # # # # # 	nserIndex = []
# # # # # # 	s = []

# # # # # # 	for i in range(n - 1, -1, -1):
# # # # # # 		while(len(s) != 0 and s[-1][0] <= arr[i]):
# # # # # # 			s.pop()

# # # # # # 		if len(s) == 0 :
# # # # # # 			nserIndex.append(n)
# # # # # # 		else:
# # # # # # 			nserIndex.append(s[-1][1])

# # # # # # 		s.append([arr[i], i])

# # # # # # 	nserIndex.reverse()
# # # # # # 	print(nserIndex)
# # # # # # 	return nserIndex

# # # # # # def maxAreaHistogram(arr, n):

# # # # # # 	nselIndexArray = nsel(arr, n)
# # # # # # 	nserIndexArray = nser(arr, n)
# # # # # # 	ans = []
# # # # # # 	maxArea = 0
# # # # # # 	for i in range(n):
# # # # # # 		ans.append((nserIndexArray[i] - nselIndexArray[i] - 1) * arr[i])
# # # # # # 		if(maxArea < ans[i]):
# # # # # # 			maxArea = ans[i]

# # # # # # 	return maxArea

# # # # # # if __name__ == '__main__':
# # # # # # 	arr = [6, 2, 5, 4, 5, 1, 6]
# # # # # # 	ans = maxAreaHistogram(arr, len(arr))
# # # # # # 	print(ans)

# # # # # lst = list(map(int, input().split()))

# # # # # print(lst)


# # # # import io
# # # # import sys


# # # # def coins(money):
# # # #     ans = 0
    
# # # #     # Check how much we can pay through 10
# # # #     while money % 10 == 0:
# # # #         ans += 1
# # # #         money -= 10
    
# # # #     # Check how much we can pay through 5
# # # #     if money:
# # # #         while money % 5 == 0:
# # # #             ans += 1
# # # #             money -= 5
    
# # # #     # If still we can't pay
# # # #     if money: return -1
    
# # # #     # Coins req
# # # #     return ans 


# # # # if __name__ == "__main__":
# # # # 	x = int(input())
# # # # 	print(coins(x))

# # # def searchInSorted(arr, N, K):
# # #         s = 0
# # #         e = N-1
# # #         mid = s + (e-s) // 2
        
# # #         while s <= e:
# # #             if arr[mid] == K: return 1
            
# # #             elif arr[mid] > K: e = mid-1
            
# # #             else: s = mid+1
            
# # #             mid = s + (e-s) // 2
        
# # #         return -1

# # # a = [1, 2, 3, 4, 6]
# # # print(searchInSorted(a, len(a), 6))

# # def countOnes(arr, N):
# #         s = 0
# #         e = N-1
# #         ans = 0
        
# #         mid = s + (e-s) // 2
        
# #         while s <= e:
            
# #             if arr[mid] == 0: e = mid - 1
            
# #             else: s = mid + 1
            
# #             mid = s + (e-s) // 2
        
        
# #         ans = (N + 1) - s  ## since strt ek position aage h and N ko index se balance karna h
# #         return ans


# # a = [1, 1, 1, 1, 1, 0, 0, 0]
# # print(countOnes(a, len(a)))

# def floorSqrt(x): 
#         s = 0
#         e = x 
        
#         mid = s + (e-s) // 2
        
#         if x == 1: return x
        
#         while s <= e:
#             if mid**2 == x: 
#                 ans = mid
#                 return mid
            
#             elif mid**2 < x: s = mid+1
            
#             else: e = mid-1
            
#             mid = s + (e-s) // 2
        
#         return floorSqrt(x-1)

# print(floorSqrt(6179767))
import io
import copy as c

def twoRepeated(arr , N):
	ans = []
	freq = c.copy(arr)
	
	for _ in range(N):
		freq[_] = 0
	
	for _ in arr:
		freq[_] += 1
		
		# Check if the elem repeated
		if freq[_] > 1: ans.append(_)

	return ans

a = [1,2,1,3,4,3]

print(twoRepeated(a, len(a)))