name = input("Enter file:")
handle = open(name)
A = []
d = dict()
for line in handle:
    if(line.startswith('From') and not(line.startswith('From:'))):
        A.append(line.split()[5].split(':')[0])
for i in A:
    d[i] = A.count(i)
for k in sorted(d):
    print(k,d[k])