def rotate(strg, n):
    return strg[n:] + strg[:n]
s = input()
rot,val = input().split()
B = ''
if(rot == 'L'):
    s1 = rotate(s,int(val))[0]
    B+=s1
print(B)