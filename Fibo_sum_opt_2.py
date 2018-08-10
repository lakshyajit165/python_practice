# Uses python3
def fibo_sum(n):
    if(n == 0):
        return(0)
    elif(n == 1):
        return(1)
    else:
        sum = 1
        A = [0*n for i in range(n+1)]
        A[0] = 0
        A[1] = 1
        for i in range(2,n+1):
            A[i] = A[i-1]+A[i-2]
            sum+=A[i]
        return(sum%10)
n = int(input())
print(fibo_sum(n))