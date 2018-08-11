# Uses python3
def fibonacci_sum(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+2):
            c = a + b
            a = b
            b = c
        return(b%10)


# Driver Program
n = int(input())
print(fibonacci_sum(n))