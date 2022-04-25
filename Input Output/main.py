#####################################
######## 1. SPACE SEPARATED 
# a = list(map(int, input().split()))
# print(a)

#####################################
######## 1. LINE SEPARATED 
a = []

# for _ in range(5):
    # a.append(int(input()))

print(a)

l=[10,20,45]
f=[20,25,30]
d=dict()
for i in range(len(f)):
    d[f[i]]=l[i]
l1=list(d.keys())
l1.sort()
print(l1)
print(d[l1[0]])
for j in range(1,len(f)):
    if(d[f[j]]>f[i-1]):
        print(d[f[j]])
    else:
        pass 
