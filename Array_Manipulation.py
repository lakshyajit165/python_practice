n,m = map(int,input().split())
A = []
for i in range(n):
    A.append(0)
while(m!=0):
    a,b,k = map(int,input().split())
    for i in range(a-1,b):
        A[i]+=k
    m-=1
print(max(A))