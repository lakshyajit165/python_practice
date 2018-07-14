n = input()
n = list(n)
flag = 0
print(n)
for i in range(len(n)):
    if(n[i] == '('):
        if(n[len(n)-1-i] == ')'):
            pass
        else:
            flag = 1
            break
    if (n[i] == '{'):
        if (n[len(n) - 1 - i] == ')}'):
            pass
        else:
            flag = 1
            break
    if (n[i] == '['):
        if (n[len(n) - 1 - i] == ']'):
            pass
        else:
            flag = 1
            break
if(flag == 1):
    print("NO")
else:
    print("YES")