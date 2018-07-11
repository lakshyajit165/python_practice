A = list(map(int,input().split(' ')))
d = int(input())
temp =[]
for i in range(d,len(A)):
    temp.append(A[i])
for i in range(d):
    temp.append(A[i])
for i in temp:
    print(i,end = ' ')