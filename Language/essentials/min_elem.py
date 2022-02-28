#################################################
####### Min & sec. min element of array

def min_elem(arr):
    min_elem = arr[0]
    sec_min_elem = arr[1]

    ## 1. Return the minimum value
    for i in arr:
        if i < min_elem: min_elem = i

    ## 2. Return the sec min value
    for i in arr:
        if i > min_elem and i < sec_min_elem: sec_min_elem = i

    return [min_elem, sec_min_elem]