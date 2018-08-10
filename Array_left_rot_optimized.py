A = list(map(int,input().split()))
d = int(input())
B = []

for i in range(len(A)):
    new_ind = (i+d)%len(A)
    B.append(A[new_ind])
    print(B)
#print(A)