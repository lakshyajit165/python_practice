a = input()
b = input()
for x in a:
    if(x == 'a'):
        a = a.replace(x,'',1)
print(a)