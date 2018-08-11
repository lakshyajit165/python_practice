def rotate(strg, n):
    return strg[n:] + strg[:n]

s = input()
t = int(input())
B = ''
while(t!=0):

    rot,val = input().split()
    if(rot == 'L'):
        B+=(rotate(s,int(val))[0])
    elif(rot == 'R'):
        B+=(rotate(s,-int(val))[0])
    t-=1
if(B in s):
    print("YES")
else:
    print("NO")
#print(rotate('HELLO', 4))