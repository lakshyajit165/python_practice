n = int(input())
for i in range(2,n):
    prime = 1
    for j in range(2,i):
        if(i%j == 0):
            prime = 0
            break
    if(prime!=0):
        print(i,end=' ')