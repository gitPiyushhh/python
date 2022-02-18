###############################################
############ 1. Filter

## Program to find all the even nums {With using anonymous fctn}

from functools import reduce


n = [1, 2, 3, 4]

evens = list(filter(lambda n: n%2 == 0 ,n))

###############################################
############ 2. Map

## Map all even no.s to double

doubles = list(map(lambda n: n*2, evens))


###############################################
############ 3. Reduce

## Accumulate all the values

ans = reduce(lambda a,b: a + b, doubles)

print(ans)