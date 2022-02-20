###########################################
######### FUNCTIONS

## Normal
def sum(a, b):
    c = a+b
    print(c)

sum(1, 2)

## Using the rest parameter 

def sum(a, *b):     # Baaki saare bache hue param b me le lo😏
    sum = a

    for i in b:
        sum += i

    print(sum)

sum(1, 2, 3, 4)


## Returning multiple values from a function

from array import *

def count_even_odd(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
        
    return even, odd


n = int(input('Enter list size: '))

arr = array('i', [])  # New array creation
for i in range(n):
    x = int(input('Number: '))
    arr.append(i)  # Adding values to the array

print(count_even_odd(arr)) ## 2 Even 3 Odd