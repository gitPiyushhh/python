
if __name__ == "__main__":
    T = int(input("Enter Test Cases: "))

    #######################################
    #######Appending to the list
    arr = []

    for _ in range(T):
        li = list(map(int, input().split()))
        arr.append(li)
    
    print(arr)

