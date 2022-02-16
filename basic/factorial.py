def fact(n):
    ans = 1

    for i in range(1, n+1):
        ## As n+1 is excluded
        ans *= i
        
    print(ans)

n = int(input("Enter the number: "))
fact(n)