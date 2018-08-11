a = input()
A = []
b = input()
B = []
count = 0
for i in range(len(a)):
    for j in range(1,len(a)):
        A.append(a[i:j+1])

for i in range(len(b)):
    for j in range(1,len(b)):
        B.append(b[i:j+1])

A = list(filter(lambda a:a!='',A))
B = list(filter(lambda a:a!='',B))
print(A)
print(B)

A = set(A)
B = set(B)
print(A^B)

