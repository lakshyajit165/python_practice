n = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
#print(A)
count = 0
sum = 0
for i in A:
    if(sum+i >= sum):
        sum+=i
        count+=1
    else:
        pass
if(sum!=0):
    print(sum,count)
else:
    print(A[0],1)
