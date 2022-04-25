from functools import cmp_to_key

def compare(a,b) :
    if a[0][1]!=b[0][1] :
        return a[0][1]-b[0][1]
        
    return a[1]-b[1]

x = [[[1, 2], 1], [[3, 4], 2], [[0, 6], 3], [[5, 7], 4], [[8, 9], 5], [[5, 9], 6]]

x = sorted(x, key=cmp_to_key(compare))

print(x)