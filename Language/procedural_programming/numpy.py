#################################################
############# Numpy: Numpy is used to store the arrays whether 1D or 2D...



#################################################
############# 1-D array

# from array import *

# arr = array('i', [])  # Creating a empty array {Of type int}

# n = int(input("Enter the no. of elem: "))
# for i in range(n):
#     x = int(input('Enter the number..'))
#     arr.append(x)       # Adding the value to array

################################################
########## Linear search

# flag = False

# for i in range(n):
#     if arr[i] == 2:
#         flag = True

# print(flag)


#################################################
############# 2-D array {By using NUMPY}
import numpy as np


############# Creating 2-D array ##############

## 1. By using array()
n = 5
arr = np.array([1, 2, 3, 4, 5])

print(arr)