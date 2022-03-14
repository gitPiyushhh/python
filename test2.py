# # ########################################
# # ####### HASH MAP IMPLEMENTATION

# # # prices = {
# # #     '6Mar': 300,
# # #     '7Mar': 400
# # # }

# # # print(prices.keys())
# # # print(prices['6Mar'] + prices['7Mar'])

# # stk = []

# # s = 'aaabbccd'
        
# # for i in s:
# #     # Empty stk
# #     if len(stk) == 0: 
# #         stk.append(i)
# #         continue
            
# #     #For rest
# #     if stk[-1] == i: 
# #         print('Popped')
# #         stk.pop(-1)
            
# #     else: stk.append(i)
        
# # print(stk)
        
# # s = ''
# # for i in range(len(stk)):
# #     s += stk.pop(-1)
        

# # stk = []
# # s = 'abcde'

# # for _ in s:
# #     stk.append(_)

# # print(stk)

# # print(6//2)


y, z= [int(i) for i in input().split()]
col = [0] + [int(i) for i in input().split()]
cutoff =[-1] + [-1 for i in range(y)]
praj = set()
l = []

for i in range(z):
  id, p, q, r, s = input().split(",")
  id = int(id[8:])
  p = float(p)
  q = int(q[2:])
  r = int(r[2:])
  s = int(s[2:])
  l.append([p, id, 1, q])
  l.append([p, id, 2, r])
  l.append([p, id, 3, s])
l.sort(key = lambda x: (-x[0], x[1], x[2]))

for i in l:
  if i[1] not in praj:
    if col[i[3]] > 0:
      col[i[3]] -= 1
      cutoff[i[3]] = i[0]
      praj.add(i[1])

col = [[col[i], i, cutoff[i]] for i in range(1, len(col))]
col.sort(key = lambda x:(-x[0], x[1], x[2]))
s = 0
for i in l:
  if i[1] not in praj:
    while s < len(col) and col[s][0] <= 0:
      s += 1
    
    if s < len(col):
      col[s][0] -= 1
      
      if col[s][2] == -1:
        col[s][2] = 100
      
      col[s][2] = min(col[s][2], i[0])
      
      praj.add(i[1])

col.sort(key = lambda x: -x[2])
for i in col:
    if i[2]!=-1:
        print("C"+str(i[1]),i[2])
    else:
        print("C"+str(i[1],"n/a"))           


# def list_string(strn):
#   level=[]
#   def permute(prefix,suffix):
#     level.append(prefix)
#     if len(suffix)==0:
#       return 
#     for i in range(len(suffix)):
#       permute(prefix,suffix[i], suffix[:i]+suffix[i+1:])
#       permute("", strn)
#       return level
    
# t = []
# t = list_string("hey")
# v = int(input())
# print(t[v])