t = int(input())
while(t!=0):
    n = int(input())
    A = [[]*n for i in range(n)]
    count = 0
    for i in range(n):
        B = list(map(int,input().split()))
        A[i] = B
    for i in range(n-1):
        for j in range(n-1):
            if(A[i][j] > A[i+1][j]):
                count+=1
            if(A[i][j] > A[i][j+1]):
                count+=1
            if(A[i][j] > A[i+1][j+1]):
                count+=1
            else:
                pass
    print(count)
    t-=1