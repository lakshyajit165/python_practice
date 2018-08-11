n = int(input())
A = list(map(int,input().split()))
count = 0
for i in A:
    if(A.count(i) > len(A)//2):
