#import math
n = int(input())
A = list(map(int,input().split()))
ans = 1
for i in A:
    ans*=i
print(ans % ((10**9)+7))