#################################################
########## Ascending order

arr = [1, 2, 3, 4]

flag = False

def check_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            flag = True
        else:
            flag = False
    return flag

#################################################
########## Descending order

def check_reverse_sorted(arr):
    for i in range(len(arr)-1, 0, -1):
        if arr[i-1] > arr[i]:
            flag = True
        else:
            flag = False
    return flag

print(check_reverse_sorted(arr))

