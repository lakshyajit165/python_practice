A = list(map(int, input().split(' ')))
x = int(input())
flag = 0
for i in A:
    if((x-i) in A):
        flag = 1
        break
if(flag):
    print("There exists a pair ({},{}) with sum = {}".format(i, x - i, x))
else:
    print("No such pair exist")

