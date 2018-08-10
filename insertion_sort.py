import random
def ins_sort(A,n):
    print("Original Array:")
    print(A)
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while(j >= 0 and key < A[j]):
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

        print("Pass: "+str(i))
        print(A)

n = int(input())
A = []
for i in range(n):
    A.append(random.randint(1,101))
ins_sort(A,n)