n,k,q = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
while(k!=0):
    temp = A[n-1]
    for i in range(n-1,0,-1):
        A[i] = A[i-1]
    A[0] = temp
    k-=1
for i in range(q):
    t = int(input())
    print(A[t])