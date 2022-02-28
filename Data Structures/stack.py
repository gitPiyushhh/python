#######################################
##### Creation {Using list}

import collections
from numpy import stack


stk = []

## Adding elements
stk.append(1)
stk.append(2)
stk.append(3)

## Removal
print(stk.pop())
print(stk.pop())
print(stk.pop())

## Empty or not
print(len(stk) == 0) ## Empty for now🙂
print(not stk) ## Empty for now🙂

#######################################
##### Creation {Using deque}

stk = collections.deque()
print(stk)

## Adding elements
stk.append(1)
stk.append(2)
stk.append(3)

## Removal
print(stk.pop())
print(stk.pop())
print(stk.pop())