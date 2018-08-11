n = int(input())
A = list(map(int, input().split()))
i = 0
swap = 0
temp = 0
while(i<len(A)):
    if(A[i] == i+1):
        i+=1
    else:
        temp = A[i]
        A[i] = A[temp-1]
        A[temp-1] = temp
        swap+=1
print(swap)
