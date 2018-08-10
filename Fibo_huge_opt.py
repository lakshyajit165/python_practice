# Uses python3
def fibonacci_sum(n,m):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a%m
    elif n == 1:
        return b%m
    else:
        for i in range(2, n+2):
            c = a + b
            a = b
            b = c
        return(b%m)


# Driver Program
n,m = map(int,input().split())
print(fibonacci_sum(n,m))