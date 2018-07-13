a = input()
b = input()

for x in a:
    if(x in b):
        a = a.replace(x,'',1)
        b = b.replace(x,'',1)
print(len(a)+len(b))