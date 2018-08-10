V = ['a','e','i','o','u','A','E','I','O','U']
s = input()
s = list(s)
for i in range(len(s)):
    if(s[i] in V):
        s[i] = ''

final = ''
for i in s:
    if(i!=''):
        final+=i
print(final)
