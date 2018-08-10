def is_matched(e):
    while (len(e) > 0):
        t = e
        e = e.replace('()', '')
        e = e.replace('{}', '')
        e = e.replace('[]', '')
        if t == e:
            return False

    return True
t = int(input())
while(t!=0):
    n = input()
    if(is_matched(n)):
        print("YES")
    else:
        print("NO")
    t-=1