<<<<<<< HEAD
# Uses python3

=======
<<<<<<< HEAD
# Uses python3
=======
t = int(input())
A = []
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        A.append(values[1])
    elif values[0] == 2:
        A.remove(A[0])
    else:
        print(A[0])
>>>>>>> 67bba19f8f38bc635f3e333cfddfd8a9527e6b34
>>>>>>> da640fa0050c6ca621a2f80c0cb8fb0a44ac2b3f
