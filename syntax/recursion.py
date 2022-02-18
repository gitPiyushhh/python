###############################################
############ 1. Factorial using recursion
def fact(n):
    ## Base cases 
    if n <= 1:
        return 1

    return n*fact(n-1)


result = fact(4)

print(result)