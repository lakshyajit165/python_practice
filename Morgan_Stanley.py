t = int(input())
B = []
for i in range(t):
    s = input()
    A = list(s)
    flag = 0
    n = int(s)
    d = n % 10
    for i in range(len(A)):
        if(int(A[i])%2 == 0 and d > int(A[i])):
            temp = A[i]
            A[i] = A[len(A)-1]
            A[len(A)-1] = temp
            flag = 1
            break
    if(flag):
        str1 = ''.join(A)
        B.append(str1)
    else:
        print(s)
for i in B:
    print(i)