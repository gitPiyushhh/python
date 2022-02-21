for i in range(1, 5):
    for j in range(1, 5):
        print("*", end='')   # We use the end = '' to tell that we dont want to change the new line
    print('\n')
    

n = 4
for i in range(1,5):
    for j in range(i):
        print("*", end='')
    print('\n')

n = 4
for i in range(1,5):
    for j in range(n-i+1):
        print("*", end='')
    print('\n')