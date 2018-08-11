import random
A = []
n = int(input())
for i in range(n*n+1):
    A.append(random.randint(1,101))
B = [A[i:i+n] for i in range(0,len(A)-1,n)]
print(B)

#printing as a 2d matrix
for i in range(len(B)):
    for j in range(len(B)):
        print(B[i][j],end = ' ')
    print()