A = list(map(int,input().split()))
d = int(input())
for i in range(d):
    temp = A[0]
    for i in range(len(A)-1):
        A[i] = A[i+1]
    A[len(A)-1] = temp
print(A)
