t = int(input())
while(t!=0):
    n = int(input())
    A = list(map(int,input().split()))
    flag = 0
    if(len(A) == 1):
        print("1")
    elif(len(A) == 2):
        print("-1")
    else:
        for i in range(1,len(A)):
            if(sum(A[:i]) == sum(A[i+1:])):
                print(i+1)
                flag = 1
                break
        if(flag == 0):
            print("-1")
    t-=1