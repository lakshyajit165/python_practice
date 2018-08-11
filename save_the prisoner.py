t = int(input())
while(t!=0):
    n,m,s = map(int,input().strip().split())
    if(s + m < n):
        print(s + m - 1)
    elif((s+m-1)%n == 0):
        print(n)
    else:
        print((s+m-1)%n)
    t-=1