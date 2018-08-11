<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> da640fa0050c6ca621a2f80c0cb8fb0a44ac2b3f
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
<<<<<<< HEAD
print(fibonacci_sum(n))
=======
print(fibonacci_sum(n))
=======
n = int(input())
A = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        print(A[i][j],end= ' ')
    print()
>>>>>>> 67bba19f8f38bc635f3e333cfddfd8a9527e6b34
>>>>>>> da640fa0050c6ca621a2f80c0cb8fb0a44ac2b3f
