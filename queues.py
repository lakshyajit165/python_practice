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