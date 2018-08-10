s = input()
flag = 0
for i in range(len(s)):
    if(s[i] == s[len(s)-1-i]):
        pass
    else:
        flag = 1
        break
if(flag):
    print("NO")
else:
    print("YES")
